# DMOJSync Plan

Export **iWolf22’s newest full AC solution per problem**, with one Git commit per changed solution. Implemented in `src/DMOJSync.py`.

## Flow

1. Load the ignored `src/.env` token with `python-dotenv`; authenticate using `Authorization: Bearer <token>`.
2. Fetch `/api/v2/user/iWolf22` and every page of `/api/v2/submissions?user=iWolf22` on every run.
3. Check `/api/v2/submission/<id>` and select the newest completed AC with full test-case marks, across languages. Reconcile exports against the account’s solved-problem list.
4. Fetch fresh metadata through `/api/v2/problems?code=...` and `/api/v2/languages`.
5. Download every selected `/src/<id>/raw` through a visible, standard Chromium session controlled with Playwright/CDP. Reuse a dedicated profile outside Git; send the token only to `dmoj.ca`. Allow browser verification, with a two-minute timeout.
6. Add metadata comments, diff the complete file, and atomically replace only changes. Commit each changed problem separately. Preserve unrelated/local edits; report incomplete exports. `--dry-run` previews diffs; `--push` uploads after success.

No cached submission or source skips: **every run refetches everything**. Reuse `httpx`, Playwright, `aiolimiter`, GitPython, `python-dotenv`, and `python-slugify`. Keep stdout logs timestamped with 🔎 ⬇️ ⏭️ ✅ ⏳ ❌ and a final coverage summary.

## Layout and names

```text
DMOJ/
├── README.md
├── PLAN.md
├── requirements.txt
├── tests/test_sync.py
├── src/
│   ├── .env          # ignored
│   ├── .gitignore
│   └── DMOJSync.py
├── ccc-2002-s1-the-students-council-breakfast.py
└── <org>-<problem-title>.<extension>
```

Use lowercase, hyphenated names without repeating the organizer prefix. Keep the problem code **in the header, not the filename**. Match files by their problem URL so title/language changes and old suffixed filenames become replacements. Stop on collisions instead of overwriting another problem.

## Solution header

```python
# Problem: CCC '20 J1 - Dog Treats (ccc20j1)
# Problem URL: https://dmoj.ca/problem/ccc20j1
# Submission: <ID and URL>
# Language: <language and runtime key>
# Submitted: <original submission date>

<original solution>
```

Use `#` for Python and `//` for C++ and C#; the account includes two accepted C# submissions. Preserve shebang/encoding declarations. Leave one blank line before the original code. Do not add fetch timestamps or duplicate headers.

## Commit format

```text
Time: 0.042 s | Memory: 8.00 MiB | Score: 100/100 | Points: 3 - DMOJSync
```

The body contains the same five metadata fields as the file header. **Score** is earned/maximum test-case score; **Points** is the problem’s point value. Values above are illustrative.

## Rate limit and verification

DMOJ documents **90 requests/minute**. Target at most **25% = 22.5/minute**; the implementation spaces requests **2.7 seconds** apart (22.22/minute). Share one limiter between API and browser requests; respect server backoff and never save challenge HTML as code. [Official API, authentication, and rate-limit documentation](https://github.com/DMOJ/docs/blob/master/docs/site/api.md).

API metadata and pagination passed live checks. Standard Chromium successfully downloaded submissions `2092598` and `2129277`; ordinary HTTP clients received Cloudflare challenges. The token format matches DMOJ’s [authentication middleware](https://github.com/DMOJ/online-judge/blob/master/judge/middleware.py).

Eight offline tests cover full-AC selection, headers, short filenames, collisions, byte-preserving idempotence, replacements, and isolated Git commits. The full export completed on November 19, 2026: **176 solutions** (143 Python, 31 C++, 2 C#), **zero failures**, and **151/151 profile solves covered**. An audit of all 176 files verified unchanged contents produce no writes or extra commits; metadata, blank lines, short filenames, and token exclusion also passed.
