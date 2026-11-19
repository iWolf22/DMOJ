# My DMOJ Solutions

My latest fully accepted [DMOJ](https://dmoj.ca) solutions, with problem and submission details at the top of each file.

**[DMOJ Profile](https://dmoj.ca/user/iWolf22) · [Sync Plan](PLAN.md) · [LeetCode Solutions](https://github.com/joshua-dierickse-alt/LeetCode)**

## DMOJSync

Solutions live in the root directory; the sync script lives in `src/`.

```bash
python -m pip install -r requirements.txt
python -m playwright install --with-deps chromium
python src/DMOJSync.py
```

Add your profile API token to the ignored `src/.env` file:

```dotenv
DMOJ_API_TOKEN=<your token>
```

Every run fetches the complete submission history and downloads the newest full AC for each problem. Identical files stay untouched; changed solutions get individual commits with runtime, memory, score, and problem points. Requests are spaced at least 2.7 seconds apart.

A visible Chromium window handles Cloudflare checks and reuses a dedicated browser profile outside the repository. Complete any interactive verification in that window if prompted.

Use `--dry-run` to preview diffs without changes, or `--push` to upload commits after a successful export. Locally edited solutions and staged changes are preserved; resolve them before syncing.

Optional environment settings: `DMOJ_BROWSER` selects an existing Chromium executable, and `DMOJ_BROWSER_PROFILE` selects a dedicated profile directory. `DMOJ_NO_SANDBOX=1` is available for restricted environments that cannot run Chromium’s sandbox.

## Checks

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests
```
