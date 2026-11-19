#!/usr/bin/env python3
"""Archive the latest full AC per DMOJ problem and commit only changed solutions."""

import argparse
import asyncio
from contextlib import asynccontextmanager
from difflib import unified_diff
import logging
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
import tempfile

from aiolimiter import AsyncLimiter
from dotenv import load_dotenv
from git import Repo
import httpx
from playwright.async_api import async_playwright, Error as BrowserError
from slugify import slugify

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://dmoj.ca'
LOG = logging.getLogger('DMOJSync')


class DMOJ:
    def __init__(self, token):
        self.token = token
        self.limiter = AsyncLimiter(1, 2.7)  # 22.22/minute, below 25% of 90/minute.
        self.http = httpx.AsyncClient(headers={'Authorization': f'Bearer {token}'}, timeout=30)

    async def api(self, path, params=None):
        for attempt in range(3):
            async with self.limiter:
                response = await self.http.get(f'{BASE}/api/v2/{path}', params=params)
            if response.headers.get('cf-mitigated') == 'challenge':
                raise RuntimeError('API challenged by Cloudflare; try again after browser verification')
            if response.status_code == 429 or response.status_code >= 500:
                delay = response.headers.get('Retry-After', '')
                delay = float(delay) if delay.isdigit() else 5 * 2**attempt
                LOG.warning('⏳ API %s: HTTP %s; waiting %.0fs', path, response.status_code, delay)
                await asyncio.sleep(delay)
                continue
            response.raise_for_status()
            return response.json()['data']
        raise RuntimeError(f'API unavailable after three attempts: {path}')

    async def pages(self, path, params=None):
        objects, page = [], 1
        while True:
            data = await self.api(path, {**(params or {}), 'page': page})
            objects.extend(data['objects'])
            LOG.info('🔎 %s: page %s, %s records', path, page, len(data['objects']))
            if not data.get('has_more', page < data.get('total_pages', page)):
                return objects
            page += 1

    @asynccontextmanager
    async def browser(self, username):
        async with async_playwright() as playwright:
            executable = os.getenv('DMOJ_BROWSER') or playwright.chromium.executable_path
            profile = os.getenv('DMOJ_BROWSER_PROFILE') or str(Path(tempfile.gettempdir()) / f'DMOJSync-{username}')
            with socket.socket() as sock:
                sock.bind(('127.0.0.1', 0))
                port = sock.getsockname()[1]
            args = [executable, f'--remote-debugging-port={port}', '--remote-debugging-address=127.0.0.1',
                    f'--user-data-dir={profile}', '--no-first-run', 'about:blank']
            if os.getenv('DMOJ_NO_SANDBOX') == '1':
                args.insert(1, '--no-sandbox')
            browser = None
            with tempfile.TemporaryFile() as diagnostics:
                process = subprocess.Popen(args, stdout=diagnostics, stderr=diagnostics)
                try:
                    for _ in range(30):
                        try:
                            browser = await playwright.chromium.connect_over_cdp(f'http://127.0.0.1:{port}')
                            break
                        except BrowserError:
                            if process.poll() is not None:
                                raise RuntimeError('Chromium exited; check browser installation/runtime libraries') from None
                            await asyncio.sleep(0.5)
                    if browser is None:
                        raise RuntimeError('Could not connect to the dedicated Chromium profile')
                    context = browser.contexts[0]

                    async def authenticate(route):
                        async with self.limiter:
                            await route.continue_(headers={**route.request.headers, 'Authorization': f'Bearer {self.token}'})

                    await context.route(f'{BASE}/**', authenticate)
                    yield await context.new_page()
                finally:
                    if browser:
                        await browser.close()
                    if process.poll() is None:
                        process.terminate()
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()

    async def source(self, page, submission):
        url = f'{BASE}/src/{submission}/raw'
        # The browser may initially receive a challenge, then reload the real source.
        async with page.expect_response(lambda r: r.url == url and r.status == 200
                                        and r.headers.get('content-type', '').startswith('text/plain'),
                                        timeout=120_000) as result:
            response = await page.goto(url, wait_until='domcontentloaded', timeout=120_000)
            if response and response.status == 403:
                LOG.warning('⏳ Browser verification required; complete any visible challenge (2 minute timeout)')
        source = await (await result.value).text()
        if not source.strip():
            raise RuntimeError(f'Empty source for submission {submission}')
        return source


def language_format(language):
    key, name = language['key'], language['common_name']
    if key.startswith(('PY', 'PYPY')) or name == 'Python':
        return 'py', '#'
    if '++' in name or key.startswith(('CPP', 'CLANGX')):
        return 'cpp', '//'
    formats = {'C': ('c', '//'), 'C#': ('cs', '//'), 'Java': ('java', '//'), 'JavaScript': ('js', '//'),
               'Rust': ('rs', '//'), 'Go': ('go', '//'), 'Ruby': ('rb', '#')}
    if name not in formats:
        raise ValueError(f'Unsupported language: {key} ({name})')
    return formats[name]


def filename(problem, extension):
    title = re.sub(r"['’](\d{2})\b", lambda m: ('20' if int(m[1]) < 70 else '19') + m[1], problem['name'])
    title = slugify(title)
    match = re.match(r'^([A-Z][A-Z0-9]+)(?=\s|[\x27’])', problem['name'])
    organizer = slugify(match[1] if match else problem['group'])
    if organizer in ('uncategorized', ''):
        organizer = 'dmoj'
    stem = title if title.startswith(organizer + '-') else f'{organizer}-{title}'
    return f'{stem}.{extension}'


def metadata(problem, submission, language):
    return [f'Problem: {problem["name"]} ({problem["code"]})',
            f'Problem URL: {BASE}/problem/{problem["code"]}',
            f'Submission: {submission["id"]} ({BASE}/submission/{submission["id"]})',
            f'Language: {language.get("short_name") or language["common_name"]} ({language["key"]})',
            f'Submitted: {submission["date"]}']


def solution_text(source, lines, prefix):
    code = source.splitlines(keepends=True)
    leading = 0
    if prefix == '#':
        leading = next((i + 1 for i, line in enumerate(code[:2]) if re.search(r'coding[:=]\s*[-\w.]+', line)), 0)
        if not leading and code and code[0].startswith('#!'):
            leading = 1
    preamble = ''.join(code[:leading])
    if preamble and not preamble.endswith('\n'):
        preamble += '\n'
    return preamble + '\n'.join(f'{prefix} {line}' for line in lines) + '\n\n' + ''.join(code[leading:])


def commit_message(submission, problem, lines):
    time = f'{submission["time"]:g} s' if submission['time'] is not None else 'N/A'
    memory = f'{submission["memory"] / 1024:.2f} MiB' if submission['memory'] is not None else 'N/A'
    subject = (f'Time: {time} | Memory: {memory} | '
               f'Score: {submission["case_points"]:g}/{submission["case_total"]:g} | '
               f'Points: {problem["points"]:g} - DMOJSync')
    return subject + '\n\n' + '\n'.join(lines)


async def latest_full_ac(client, candidates, code):
    for candidate in candidates:
        if candidate['problem'] == code and candidate['result'] == 'AC':
            submission = (await client.api(f'submission/{candidate["id"]}'))['object']
            if (submission['status'] == 'D' and submission['result'] == 'AC'
                    and submission['case_points'] == submission['case_total']):
                return submission
    return None


def managed_solutions(root):
    solutions = {}
    for path in root.iterdir():
        if path.is_file() and path.suffix in {'.py', '.cpp', '.cs', '.c', '.java', '.js', '.rs', '.go', '.rb'}:
            header = path.read_bytes()[:1000].decode('utf-8', errors='replace')
            match = re.search(r'^(?:#|//) Problem URL: https://dmoj\.ca/problem/([\w]+)\r?$', header, re.MULTILINE)
            if match:
                solutions.setdefault(match[1], []).append(path)
    return solutions


def save_solution(repo, problem, name, content, message, dry_run, known_paths=None):
    root = Path(repo.working_tree_dir)
    target = root / name
    old = sorted(managed_solutions(root).get(problem['code'], []) if known_paths is None else known_paths)
    for path in set(old + ([target] if target.exists() else [])):
        managed = f'Problem URL: {BASE}/problem/{problem["code"]}' in path.read_bytes().decode('utf-8')[:1000]
        if not managed or repo.git.status('--porcelain', '--', path.name):
            raise RuntimeError(f'Preserving locally modified or unmanaged file: {path.name}')
    previous = target.read_bytes().decode('utf-8') if target.exists() else ''
    obsolete = [path for path in old if path != target]
    if target.exists() and previous == content and not obsolete:
        return False
    if dry_run:
        print(''.join(unified_diff(previous.splitlines(True), content.splitlines(True), fromfile=name, tofile=name)), end='')
        for path in obsolete:
            LOG.info('🔎 Would remove %s', path.name)
        return True
    if repo.index.diff('HEAD'):
        raise RuntimeError('Preserving staged changes; commit or unstage them before syncing')
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='', dir=root, delete=False) as temp:
        temp.write(content)
    temporary = Path(temp.name)
    try:
        temporary.replace(target)
        repo.index.add([name])
        if obsolete:
            repo.index.remove([path.name for path in obsolete], working_tree=True)
        repo.index.commit(message)
    finally:
        temporary.unlink(missing_ok=True)
    return True


async def sync(args):
    repo = Repo(ROOT)
    if repo.index.diff('HEAD'):
        raise RuntimeError('Preserving staged changes; commit or unstage them before syncing')
    load_dotenv(ROOT / 'src/.env')
    token = os.getenv('DMOJ_API_TOKEN')
    if not token:
        raise RuntimeError('Set DMOJ_API_TOKEN in src/.env')
    client = DMOJ(token)
    changed = unchanged = failed = 0
    exported = set()
    try:
        user = (await client.api(f'user/{args.user}'))['object']
        submissions = await client.pages('submissions', {'user': args.user})
        languages = {entry['key']: entry for entry in await client.pages('languages')}
        codes = sorted({entry['problem'] for entry in submissions if entry['result'] == 'AC'})
        problems = {}
        for start in range(0, len(codes), 50):
            for problem in await client.pages('problems', {'code': codes[start:start + 50]}):
                problems[problem['code']] = problem
        LOG.info('🔎 %s submissions; %s solved problems; %s AC problem candidates', len(submissions), user['problem_count'], len(codes))
        candidates = sorted(submissions, key=lambda s: (s['date'], s['id']), reverse=True)
        managed = managed_solutions(ROOT)
        async with client.browser(args.user) as page:
            for code in codes:
                try:
                    problem = problems[code]
                    submission = await latest_full_ac(client, candidates, code)
                    if submission is None:
                        LOG.info('⏭️ %s: no completed full AC', code)
                        continue
                    language = languages[submission['language']]
                    extension, prefix = language_format(language)
                    LOG.info('⬇️ [%s/%s] %s — submission %s', len(exported) + failed + 1, len(codes), code, submission['id'])
                    source = await client.source(page, submission['id'])
                    lines = metadata(problem, submission, language)
                    content = solution_text(source, lines, prefix)
                    changed_file = save_solution(repo, problem, filename(problem, extension), content,
                                                 commit_message(submission, problem, lines), args.dry_run, managed.get(code, []))
                    changed += changed_file
                    unchanged += not changed_file
                    exported.add(code)
                    LOG.info('%s %s', ('🔎 Would commit' if args.dry_run else '✅ Committed') if changed_file else '⏭️ Unchanged', code)
                except Exception as error:
                    failed += 1
                    LOG.error('❌ %s: %s', code, error)
        missing = set(user['solved_problems']) - exported
        LOG.info('📊 %s changed, %s unchanged, %s failed; %s/%s expected solves covered',
                 changed, unchanged, failed, len(set(user['solved_problems']) & exported), len(user['solved_problems']))
        if missing:
            LOG.error('❌ Missing solved problems: %s', ', '.join(sorted(missing)))
        if failed or missing:
            raise RuntimeError('Incomplete export; rerun after resolving the errors above')
        if args.push and not args.dry_run:
            repo.git.push()
            LOG.info('🚀 Pushed commits')
    finally:
        await client.http.aclose()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--user', default='iWolf22')
    parser.add_argument('--dry-run', action='store_true', help='Fetch everything and show diffs without writing or committing')
    parser.add_argument('--push', action='store_true', help='Push after a complete successful export')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%H:%M:%S', stream=sys.stdout)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    try:
        asyncio.run(sync(parser.parse_args()))
    except (Exception, KeyboardInterrupt) as error:
        LOG.error('❌ %s', error or 'Interrupted')
        sys.exit(1)
