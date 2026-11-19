# DMOJSync Plan

Archive **iWolf22’s newest full AC solution per problem**, refetch everything each run, and automatically commit changed solutions. **Implemented in `src/DMOJSync.py`; full export validation follows the first run.**

## API and scraping flow

Load `src/.env` with `python-dotenv`; authenticate requests to `https://dmoj.ca` using `Authorization: Bearer <token>`. `src/.gitignore` excludes that environment file.

1. **Discover:** `GET /api/v2/user/iWolf22` for solved problems; paginate `GET /api/v2/submissions?user=iWolf22` for the complete submission history.
2. **Select:** use `GET /api/v2/submission/<id>` to verify completed judging and full test-case marks; select the newest full AC per problem.
3. **Enrich:** `GET /api/v2/problem/<code>` for title, group, and problem points; `GET /api/v2/languages` for language metadata.
4. **Download:** open authenticated `/src/<id>/raw` in a standard, visible Chromium session controlled through Playwright/CDP. Let the browser complete Cloudflare’s JavaScript check and reuse its dedicated profile between runs. Attach the token only to requests to `dmoj.ca`. JSON submission responses do not include source code.
5. **Sync:** prepend the metadata comments below → diff the complete file → replace only changes → create one stats commit per changed problem.

Refetch all pages, metadata, and selected sources every run. Sources: [official API/authentication documentation](https://github.com/DMOJ/docs/blob/master/docs/site/api.md), [raw source route](https://github.com/DMOJ/online-judge/blob/master/dmoj/urls.py).

## Endpoint test results — November 19, 2026

Tested with the local token; endpoint probes were spaced at least 2.7 seconds apart. Token values and downloaded contents were not printed.

| Endpoint tested | Result |
| --- | --- |
| `/api/v2/user/iWolf22` | 200; valid JSON |
| `/api/v2/submissions?user=iWolf22` | 200; 1,000 submissions |
| Same endpoint with `&page=2` | 200; remaining 73 submissions (1,073 total) |
| `/api/v2/languages` | 200; 75 languages |
| `/api/v2/problem/nccc7j1` | 200; valid JSON |
| `/api/v2/submission/2092598` and `/2129277` | Both 200; valid JSON |
| Raw source and HTML source pages via ordinary HTTP clients | 403; Cloudflare challenge |
| `/src/2092598/raw` via standard Chromium | 200; 220 bytes of plain-text source; valid Python syntax |
| `/src/2129277/raw` via standard Chromium | 200; 136 bytes of plain-text source |

**Source access is verified.** A standard Chromium launch completed the JavaScript challenge; reopening the same isolated profile downloaded both sources immediately with HTTP 200. Plain `requests`, browser-compatible `curl_cffi`, and the default automated browser launch did not clear the challenge in these tests. No CAPTCHA service, proxy, or account password was used. The sync and Git behavior are implemented and covered by offline tests; the first full export is the remaining live check.

The token/header was correct: DMOJ’s [authentication middleware](https://github.com/DMOJ/online-judge/blob/master/judge/middleware.py) and an [existing submission downloader](https://github.com/0foxes/submission-downloader/blob/master/submission_downloader.py) use the same Bearer header. The failures carried Cloudflare’s documented [`cf-mitigated: challenge` marker](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/).

## Repository and filenames

```text
DMOJ/
├── README.md
├── PLAN.md
├── requirements.txt
├── src/
│   ├── .env                 # local token; ignored
│   ├── .gitignore           # ignores /.env
│   └── DMOJSync.py
├── ccc-2020-j1-dog-treats.py
└── <org>-<problem-title>.<extension>
```

Use the contest/organizer label (e.g. `ccc`), followed by the title without repeating the organizer prefix. Lowercase hyphenated names; use `dmoj` if no organizer is identifiable. Keep the problem code in the header, not the filename; match existing files through their problem URL, including files using the old suffix. Stop on filename collisions instead of overwriting another problem. Extensions follow the submission language. All solutions live directly in the root.

## Sync behavior

1. **Small Python file:** focused functions; reuse `httpx` for JSON, Playwright for browser source downloads, `python-dotenv`, `aiolimiter`, GitPython, and `python-slugify`. No HTML parser needed. Command: `python src/DMOJSync.py`. Keep the dedicated browser profile outside the repository; never log or commit credentials.
2. **Full refresh:** traverse every history page and refetch problem metadata and selected source every run. No cache-based skipping. Choose the newest completed AC with full test-case marks across languages; break date ties by submission ID.
3. **Check coverage:** reconcile full solves with the authenticated account’s solved-problem list/count. Report inaccessible pages/sources and missing problem codes; mark incomplete runs clearly. Never delete files because a page became inaccessible.
4. **Idempotent files:** diff content; identical files produce no writes or commits. Download and validate before atomically replacing changed files. Remove the previous managed filename on title/language changes and commit the replacement together. Preserve unrelated files and local edits.
5. **Automatic commits:** one commit per changed problem, staging only its managed paths. Provide `--dry-run` with diffs and optional `--push`.
6. **Stdout logging:** timestamps and 🔎 discovery, ⬇️ fetch, ⏭️ unchanged, ✅ commit, ⏳ retry, ❌ failure; finish with changed/unchanged/inaccessible counts.

## Request pacing

The [official documentation](https://github.com/DMOJ/docs/blob/master/docs/site/api.md#rate-limiting) states **90 requests/minute** and warns of CAPTCHA enforcement. Use **25% = 22.5/minute**, at least **2.667 seconds between requests**. One shared limiter covers API calls and browser requests to DMOJ, including retries and redirects; no concurrent bursts. Honor `Retry-After` and back off on temporary failures. Let the visible browser handle JavaScript checks; pause for user action if an interactive CAPTCHA appears. Never save challenge HTML as source.

## Selected commit format

```text
Time: 0.042 s | Memory: 8.0 MB | Score: 100/100 | Points: 3 - DMOJSync

Problem: CCC '20 J1 - Dog Treats (ccc20j1)
Problem URL: https://dmoj.ca/problem/ccc20j1
Submission: <ID and URL>
Language: <language>
Submitted: <original submission date>
```

Illustrative statistics: **Score** is earned/maximum test-case score; **Points** is the problem’s DMOJ point value. Use reported values and units, without invented percentiles. This follows your [LeetSync format](https://github.com/joshua-dierickse-alt/LeetCode/commit/c906b40360c0b9606880775fa54b22d62d9573d5).

## Solution header

Every saved solution starts with this metadata, followed by **one blank line**, then the original code:

```python
# Problem: CCC '20 J1 - Dog Treats (ccc20j1)
# Problem URL: https://dmoj.ca/problem/ccc20j1
# Submission: <ID and URL>
# Language: <language>
# Submitted: <original submission date>

<original solution>
```

Use `#` for Python and `//` for C++ and C# (two accepted C# submissions were found during the export). Keep a small extension-to-comment-prefix mapping for any additional supported languages; report unknown languages rather than guessing. Preserve required shebang/encoding declarations before the metadata if present. Build the header afresh from submission metadata each run, without duplication or fetch timestamps, then diff the header and code together.

## Validation and README

Verify pagination, full-AC selection, coverage reporting, pacing, filename collisions/renames, and isolated commits. An identical second run must refetch everything and produce zero changes/commits. The README includes setup, the command, dry-run/push options, and browser requirements.
