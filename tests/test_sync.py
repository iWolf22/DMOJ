"""Offline checks for file safety, metadata, and per-problem Git commits."""
import importlib.util
import asyncio
from pathlib import Path
import tempfile
import unittest

from git import Repo

spec = importlib.util.spec_from_file_location('dmoj_sync', Path(__file__).parents[1] / 'src/DMOJSync.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.problem = {'code': 'ccc20j1', 'name': "CCC '20 J1 - Dog Treats", 'group': 'CCC', 'points': 3}
        self.submission = {'id': 42, 'date': '2020-02-12T12:00:00Z', 'time': 0.042, 'memory': 8192,
                           'case_points': 100, 'case_total': 100}
        self.language = {'key': 'PY3', 'common_name': 'Python', 'short_name': 'Python 3'}
        self.lines = sync.metadata(self.problem, self.submission, self.language)

    def test_filename_includes_organizer_and_year_without_code_suffix(self):
        self.assertEqual(sync.filename(self.problem, 'py'), 'ccc-2020-j1-dog-treats.py')

    def test_python_and_cpp_comments_leave_blank_line(self):
        for language, name, prefix in [('PY3', 'Python', '#'), ('CPP17', 'C++', '//'), ('MONOCS', 'C#', '//')]:
            extension, actual = sync.language_format({'key': language, 'common_name': name})
            text = sync.solution_text('original\n', self.lines, actual)
            self.assertTrue(text.startswith(prefix + ' Problem:'))
            self.assertTrue(text.endswith('\n\noriginal\n'))
        with self.assertRaises(ValueError):
            sync.language_format({'key': 'TEXT', 'common_name': 'Plain Text'})

    def test_shebang_and_encoding_remain_first(self):
        source = '#!/usr/bin/python\n# coding: utf-8\nprint(1)\n'
        text = sync.solution_text(source, self.lines, '#')
        self.assertTrue(text.startswith('#!/usr/bin/python\n# coding: utf-8\n# Problem:'))
        self.assertEqual(text.count('Problem URL:'), 1)

    def test_empty_language_label_falls_back_to_name_and_runtime_key(self):
        lines = sync.metadata(self.problem, self.submission, {**self.language, 'short_name': ''})
        self.assertIn('Language: Python (PY3)', lines)

    def test_commit_stats_distinguish_test_score_and_problem_points(self):
        message = sync.commit_message(self.submission, self.problem, self.lines)
        self.assertIn('Time: 0.042 s | Memory: 8.00 MiB | Score: 100/100 | Points: 3 - DMOJSync', message)
        self.assertIn('Submission: 42 (https://dmoj.ca/submission/42)', message)

    def test_newest_partial_or_rejudged_ac_does_not_replace_full_ac(self):
        records = {4: {'status': 'D', 'result': 'WA', 'case_points': 0, 'case_total': 100},
                   3: {'status': 'D', 'result': 'AC', 'case_points': 50, 'case_total': 100},
                   2: {'status': 'G', 'result': 'AC', 'case_points': 100, 'case_total': 100},
                   1: {'status': 'D', 'result': 'AC', 'case_points': 100, 'case_total': 100}}
        class Client:
            async def api(self, path):
                number = int(path.split('/')[-1])
                return {'object': {'id': number, **records[number]}}
        candidates = [{'id': number, 'problem': 'sample', 'result': 'AC'} for number in (4, 3, 2, 1)]
        selected = asyncio.run(sync.latest_full_ac(Client(), candidates, 'sample'))
        self.assertEqual(selected['id'], 1)
        self.assertIsNone(asyncio.run(sync.latest_full_ac(Client(), candidates, 'missing')))

    def test_git_idempotence_replacement_and_unrelated_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = Repo.init(root)
            with repo.config_writer() as config:
                config.set_value('user', 'name', 'Sync Test')
                config.set_value('user', 'email', 'test@example.com')
            (root / 'README.md').write_text('initial\n')
            repo.index.add(['README.md'])
            repo.index.commit('initial')
            (root / 'README.md').write_text('unrelated local edit\n')
            name = sync.filename(self.problem, 'py')
            content = sync.solution_text('print(1)\r\n', self.lines, '#')
            save = lambda filename, text, dry=False: sync.save_solution(repo, self.problem, filename, text, 'stats', dry)
            self.assertTrue(save(name, content))
            head = repo.head.commit.hexsha
            mtime = (root / name).stat().st_mtime_ns
            self.assertFalse(save(name, content))
            self.assertEqual(repo.head.commit.hexsha, head)
            self.assertEqual((root / name).stat().st_mtime_ns, mtime)
            self.assertEqual((root / name).read_bytes(), content.encode())
            self.assertEqual(list(repo.head.commit.stats.files), [name])
            with self.assertRaises(RuntimeError):
                sync.save_solution(repo, {**self.problem, 'code': 'different'}, name, content, 'collision', False)
            self.assertTrue(save(name, content.replace('print(1)', 'print(2)'), dry=True))
            self.assertEqual(repo.head.commit.hexsha, head)
            new_name = sync.filename(self.problem, 'cpp')
            self.assertTrue(save(new_name, sync.solution_text('int main() {}\n', self.lines, '//')))
            self.assertFalse((root / name).exists())
            self.assertEqual(set(repo.head.commit.stats.files), {name, new_name})
            self.assertEqual((root / 'README.md').read_text(), 'unrelated local edit\n')
            (root / new_name).write_text('local solution edit\n')
            with self.assertRaises(RuntimeError):
                save(new_name, content)
            self.assertEqual((root / new_name).read_text(), 'local solution edit\n')

    def test_unmanaged_or_staged_files_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = Repo.init(root)
            with repo.config_writer() as config:
                config.set_value('user', 'name', 'Sync Test')
                config.set_value('user', 'email', 'test@example.com')
            (root / 'README.md').write_text('initial')
            repo.index.add(['README.md'])
            repo.index.commit('initial')
            name = sync.filename(self.problem, 'py')
            (root / name).write_text('my untracked file')
            with self.assertRaises(RuntimeError):
                sync.save_solution(repo, self.problem, name, 'new', 'stats', False)
            self.assertEqual((root / name).read_text(), 'my untracked file')
            (root / name).unlink()
            (root / 'README.md').write_text('staged edit')
            repo.index.add(['README.md'])
            with self.assertRaises(RuntimeError):
                sync.save_solution(repo, self.problem, name, 'new', 'stats', False)
            self.assertFalse((root / name).exists())


if __name__ == '__main__':
    unittest.main()
