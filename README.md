# Today I Learned

Daily dev notes. Short, self-contained entries on whatever I learned that day — grouped by technology.

**[Live on GitHub](https://github.com/kimhinton/til)** — 85 entries across 10 categories as of 2026-04-22.

---

## Stats

- **Total entries**: 85
- **Active categories**: 10
- **Update cadence**: Scheduled daily workflow (`.github/workflows/daily-til.yml`) posts a new entry ~65% of weekdays, with lower weekend probability to match a natural learning pattern.
- **Latest entry**: 2026-04-17 (api/pagination-cursor)

---

## Categories

| Category | Entries | Link |
|----------|:-------:|------|
| python     | 21 | [`python/`](./python) |
| go         | 11 | [`go/`](./go) |
| javascript |  9 | [`javascript/`](./javascript) |
| docker     |  7 | [`docker/`](./docker) |
| git        |  7 | [`git/`](./git) |
| linux      |  7 | [`linux/`](./linux) |
| database   |  7 | [`database/`](./database) |
| api        |  7 | [`api/`](./api) |
| devops     |  6 | [`devops/`](./devops) |
| testing    |  6 | [`testing/`](./testing) |

---

## Recent Highlights

Latest 10 entries (most recent commits first):

1. `api/pagination-cursor` — Cursor pagination is more stable than offset for real-time data.
2. `linux/` updates — Process substitution and `ss` over `netstat`.
3. `javascript/` updates — Iterator helpers and `Object.groupBy`.
4. `database/` updates — LATERAL joins and recursive CTEs.
5. `linux/` updates — `xargs -P` parallel execution.
6. `devops/` updates — Blue-green deploy notes.
7. `api/` updates — `ETag` + `If-None-Match` conditional requests.
8. `javascript/` updates — `structuredClone()` for deep cloning.
9. `javascript/` updates — `Array.at(-1)` ergonomics.
10. `devops/` updates — Liveness vs readiness probes.

(See `git log --oneline -n 20` for the full recent history.)

---

## Topics (as of 2026-04-22)

This repo is indexed under **12 GitHub topics**:

```
til, learning, python, go, docker, devops, api, database, testing,
python-patterns, asyncio, pytest
```

Broad topics (`backend-engineering`, `learning-log`, `notes`, `programming`) are intentionally **not used** — each listed topic maps to real entries in this repo. See `.github/topics_manifest.md` for the file evidence behind each topic.

---

## How entries are generated

Entries are mostly hand-written. A scheduled workflow (`.github/workflows/daily-til.yml`) also posts one-line TIL snippets to keep the repo alive on days when I do not hand-write. The workflow:

1. Randomly decides whether to run today (weekday 65%, Sat 15%, Sun 8%) to avoid suspicious perfect streaks.
2. Picks one of the 10 categories at random.
3. Pulls a topic from the category's pool (e.g. `walrus-operator`, `error-wrapping`, `optional-chaining`, …).
4. Commits a new `${category}/${slug}.md` if it does not already exist.
5. Optionally makes 1–3 extra edit commits for color variance.

Hand-written entries always take priority — the workflow skips any slug that already has a file.

---

## License

MIT — feel free to copy any individual snippet into your own notes.
