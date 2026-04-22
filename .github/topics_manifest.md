# til GitHub Topics Manifest

**Last updated**: 2026-04-22
**Total topics**: 12
**Previous state**: 0 (new)
**Update API**: `PUT /repos/kimhinton/til/topics`

---

## Current topics (12)

```
til, learning, python, go, docker, devops, api, database, testing,
python-patterns, asyncio, pytest
```

---

## Topic rationale (evidence-based)

Conditional commitment #2: remove broad topics + add ≥4 specific replacements. No topics without concrete file evidence.

| Topic | File evidence | Files |
|-------|---------------|:-----:|
| `til` | Repo identity (root README + 10 categories) | — |
| `learning` | Repo purpose ("daily dev notes") | — |
| `python` | `python/` directory | 21 |
| `go` | `go/` directory | 11 |
| `docker` | `docker/` directory | 7 |
| `devops` | `devops/` directory | 6 |
| `api` | `api/` directory | 7 |
| `database` | `database/` directory | 7 |
| `testing` | `testing/` directory | 6 |
| `python-patterns` | `python/{walrus-operator, dataclasses-frozen, contextmanager, functools-cache, pathlib-over-os, structural-pattern-matching, typing-protocol, slots-dataclass, dict-merge-operator, ...}.md` — most python entries are language patterns/idioms | 20+ |
| `asyncio` | `python/asyncio-gather.md` | 1+ |
| `pytest` | `testing/fixture-scope.md` (pytest-specific concept) | 1 |

---

## Excluded topics + rationale

### Broad topics

Started from 0 topics, so **no broad topics to remove**.
Forbidden for future addition:

- `backend-engineering` — no file evidence. Too broad.
- `learning-log` — duplicates `learning`; no added value.
- `notes` — too broad.
- `programming`, `coding` — no file evidence. Adds noise to GitHub search.

### Topics skipped due to missing file evidence

| Topic | Status | Reason |
|-------|--------|--------|
| `sqlalchemy` | **SKIP** | No ORM-specific files in `database/`. `explain-analyze, lateral-join, partial-index, recursive-cte, upsert-on-conflict, window-functions` are all generic SQL topics. Avoids false signal. |
| `fastapi` | **SKIP** | No FastAPI-specific files in `api/`. `cursor-pagination, etag-caching, hateoas-links, idempotency-key, rate-limit-headers` are all generic protocol/REST topics. |

→ Add the corresponding topic once a FastAPI- or SQLAlchemy-specific entry is written.

---

## Verification

```bash
# Applied update command (executed)
gh api -X PUT repos/kimhinton/til/topics \
  -f 'names[]=til' -f 'names[]=learning' \
  -f 'names[]=python' -f 'names[]=go' -f 'names[]=docker' \
  -f 'names[]=devops' -f 'names[]=api' -f 'names[]=database' \
  -f 'names[]=testing' -f 'names[]=python-patterns' \
  -f 'names[]=asyncio' -f 'names[]=pytest'

# Verification commands
gh api repos/kimhinton/til/topics --jq '.names | length'   # → 12
gh api repos/kimhinton/til/topics --jq '.names'             # → 12-item array
```

**Result verification**
- [x] topics increased from 0 → 12
- [x] 3 specific topics included (`python-patterns`, `asyncio`, `pytest`). 2 of the 4 originally proposed specific topics (`sqlalchemy`, `fastapi`) skipped due to missing file evidence.
- [x] All broad topics (`backend-engineering`, `learning-log`, `notes`) absent
- [x] Every topic has file- or directory-level evidence

---

## Follow-up

- Once ≥1 SQLAlchemy-specific TIL is written → `sqlalchemy` topic can be added.
- Once ≥1 FastAPI-specific TIL is written → `fastapi` topic can be added.
