"""
Backfill TIL repo with 1 year of natural-looking commits.
Each commit creates a real TIL markdown file with actual dev content.
Dates are backdated with workHours distribution.
"""

import os
import random
import subprocess
from datetime import datetime, timedelta

# TIL content pool - real, useful dev notes
TILS = {
    "python": [
        ("walrus-operator", "The walrus operator `:=` assigns and returns a value in a single expression. Useful in while loops and comprehensions.", "if (n := len(data)) > 10:\n    print(f'{n} items')"),
        ("dataclasses-frozen", "Use `@dataclass(frozen=True)` to create immutable instances. Raises `FrozenInstanceError` on attribute assignment.", "@dataclass(frozen=True)\nclass Point:\n    x: float\n    y: float"),
        ("contextmanager", "`contextlib.contextmanager` turns a generator into a context manager. `yield` separates setup from teardown.", "@contextmanager\ndef timer():\n    start = time.time()\n    yield\n    print(f'{time.time()-start:.2f}s')"),
        ("dict-merge-operator", "Python 3.9+ supports dict merging with the `|` operator.", "merged = dict1 | dict2\ndict1 |= dict2  # in-place"),
        ("pathlib-over-os", "`pathlib.Path` is more readable than `os.path` for file operations.", "path = Path('data') / 'file.csv'\ncontent = path.read_text()"),
        ("functools-cache", "`@functools.cache` provides unlimited memoization. Use `@lru_cache(maxsize=N)` for bounded cache.", "@cache\ndef fib(n):\n    return n if n < 2 else fib(n-1) + fib(n-2)"),
        ("structural-pattern-matching", "Python 3.10 `match/case` supports structural pattern matching with guards.", "match command:\n    case ['go', direction] if direction in VALID:\n        move(direction)\n    case _:\n        print('unknown')"),
        ("enumerate-start", "`enumerate()` accepts a `start` parameter for custom index offset.", "for i, item in enumerate(items, start=1):\n    print(f'{i}. {item}')"),
        ("itertools-chain", "`itertools.chain` flattens multiple iterables without creating intermediate lists.", "from itertools import chain\nall_items = list(chain(list1, list2, list3))"),
        ("typing-protocol", "`typing.Protocol` enables structural subtyping (duck typing with type hints).", "class Drawable(Protocol):\n    def draw(self) -> None: ..."),
        ("slots-dataclass", "`__slots__` in dataclasses reduces memory footprint by preventing `__dict__` creation.", "@dataclass(slots=True)\nclass Vector:\n    x: float\n    y: float"),
        ("asyncio-gather", "`asyncio.gather` runs multiple coroutines concurrently and collects results.", "results = await asyncio.gather(\n    fetch(url1),\n    fetch(url2),\n    fetch(url3)\n)"),
        ("collections-counter", "`Counter.most_common(n)` returns the n most frequent elements.", "from collections import Counter\nCounter(words).most_common(5)"),
        ("string-removeprefix", "`str.removeprefix()` and `str.removesuffix()` added in Python 3.9. Cleaner than slicing.", "'test_file.py'.removeprefix('test_')  # 'file.py'"),
        ("generator-send", "`generator.send()` pushes a value into a paused generator at `yield`.", "def accumulator():\n    total = 0\n    while True:\n        total += yield total"),
        ("any-all-generators", "`any()` and `all()` short-circuit on generator expressions.", "has_error = any(r.status >= 400 for r in responses)"),
        ("defaultdict", "`defaultdict` auto-creates missing keys with a factory function.", "from collections import defaultdict\ncounts = defaultdict(int)\ncounts['a'] += 1"),
        ("zip-strict", "`zip(..., strict=True)` in Python 3.10+ raises ValueError on unequal lengths.", "for a, b in zip(names, scores, strict=True):\n    print(f'{a}: {b}')"),
        ("pdb-breakpoint", "`breakpoint()` is a built-in that replaces `import pdb; pdb.set_trace()`.", "def process(data):\n    breakpoint()  # drops into debugger\n    return transform(data)"),
        ("starred-assignment", "Extended unpacking with `*` captures remaining items into a list.", "first, *middle, last = [1, 2, 3, 4, 5]\n# first=1, middle=[2,3,4], last=5"),
    ],
    "go": [
        ("error-wrapping", "Use `fmt.Errorf` with `%w` to wrap errors for `errors.Is/As` unwrapping.", 'return fmt.Errorf("query failed: %w", err)'),
        ("defer-stack", "Deferred calls execute LIFO (last in, first out). Useful for cleanup.", "f, _ := os.Open(name)\ndefer f.Close()"),
        ("context-timeout", "`context.WithTimeout` cancels downstream work after a deadline.", "ctx, cancel := context.WithTimeout(ctx, 5*time.Second)\ndefer cancel()"),
        ("sync-once", "`sync.Once` ensures a function runs exactly once across goroutines.", "var once sync.Once\nonce.Do(func() { db = connectDB() })"),
        ("embed-directive", "`go:embed` embeds files into the binary at compile time.", '//go:embed config.json\nvar configJSON []byte'),
        ("table-driven-tests", "Table-driven tests use a slice of test cases for exhaustive coverage.", 'tests := []struct {\n    input string\n    want  int\n}{\n    {"hello", 5},\n    {"", 0},\n}'),
        ("slog-structured-logging", "`log/slog` provides structured logging with key-value pairs (Go 1.21+).", 'slog.Info("request",\n    "method", r.Method,\n    "path", r.URL.Path,\n)'),
        ("channels-direction", "Directional channels enforce send-only or receive-only at compile time.", "func producer(ch chan<- int) {\n    ch <- 42\n}"),
        ("goroutine-leak", "Always ensure goroutines can exit. Use context cancellation or done channels.", "go func() {\n    select {\n    case <-done:\n        return\n    case ch <- val:\n    }\n}()"),
        ("interface-check", "Compile-time interface compliance check with blank identifier.", "var _ io.Reader = (*MyReader)(nil)"),
    ],
    "javascript": [
        ("optional-chaining", "Optional chaining `?.` short-circuits to `undefined` if a reference is nullish.", "const city = user?.address?.city"),
        ("structuredclone", "`structuredClone()` deep-clones objects including nested structures and circular refs.", "const copy = structuredClone(original)"),
        ("array-at", "`Array.at(-1)` returns the last element without `.length` calculation.", "const last = arr.at(-1)"),
        ("promise-allsettled", "`Promise.allSettled` waits for all promises regardless of rejection.", "const results = await Promise.allSettled([p1, p2, p3])"),
        ("nullish-coalescing", "The `??` operator returns the right operand only for `null`/`undefined`, not falsy.", "const port = config.port ?? 3000"),
        ("object-groupby", "`Object.groupBy()` groups array elements by a callback return value.", "Object.groupBy(people, p => p.age >= 18 ? 'adult' : 'minor')"),
        ("abortcontroller", "`AbortController` cancels fetch requests and other async operations.", "const ctrl = new AbortController()\nfetch(url, { signal: ctrl.signal })\nctrl.abort()"),
        ("temporal-api", "Temporal API replaces Date with better timezone and calendar support.", "const now = Temporal.Now.zonedDateTimeISO()"),
    ],
    "docker": [
        ("multi-stage-build", "Multi-stage builds reduce final image size by copying only artifacts.", "FROM node:20 AS build\nRUN npm run build\nFROM nginx:alpine\nCOPY --from=build /app/dist /usr/share/nginx/html"),
        ("healthcheck", "`HEALTHCHECK` instruction tells Docker how to test container health.", "HEALTHCHECK --interval=30s CMD curl -f http://localhost/ || exit 1"),
        ("buildkit-cache-mount", "BuildKit cache mounts speed up package installation across builds.", "RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt"),
        ("compose-profiles", "Docker Compose profiles selectively start services for different environments.", "services:\n  debug:\n    profiles: [debug]\n    image: busybox"),
        ("no-root-user", "Run containers as non-root for security. Create a dedicated user.", "RUN adduser -D appuser\nUSER appuser"),
        ("layer-caching", "Order Dockerfile instructions from least to most frequently changing for cache efficiency.", "COPY package.json .\nRUN npm install\nCOPY . .  # source changes don't bust npm cache"),
    ],
    "git": [
        ("bisect", "`git bisect` uses binary search to find the commit that introduced a bug.", "git bisect start\ngit bisect bad HEAD\ngit bisect good v1.0"),
        ("worktree", "`git worktree` lets you check out multiple branches simultaneously in separate dirs.", "git worktree add ../hotfix hotfix-branch"),
        ("reflog-recovery", "`git reflog` shows all reference updates. Recover lost commits after reset.", "git reflog\ngit reset --hard HEAD@{3}"),
        ("stash-patch", "`git stash -p` lets you selectively stash changes hunk by hunk.", "git stash push -p -m 'partial save'"),
        ("rerere", "`git rerere` remembers how you resolved merge conflicts and auto-applies next time.", "git config rerere.enabled true"),
        ("commit-fixup", "`git commit --fixup` + `rebase --autosquash` for clean history.", "git commit --fixup abc123\ngit rebase -i --autosquash main"),
    ],
    "linux": [
        ("xargs-parallel", "`xargs -P` runs commands in parallel across multiple CPU cores.", "find . -name '*.jpg' | xargs -P4 -I{} convert {} -resize 50% {}"),
        ("ss-over-netstat", "`ss` is faster than deprecated `netstat` for socket statistics.", "ss -tulnp | grep :8080"),
        ("journalctl-follow", "`journalctl -fu` follows logs for a specific systemd service.", "journalctl -fu nginx --since '5 min ago'"),
        ("process-substitution", "Process substitution `<()` lets you diff command outputs directly.", "diff <(ls dir1) <(ls dir2)"),
        ("heredoc-cat", "Here-documents write multi-line content to files without echo chains.", "cat <<'EOF' > config.yml\nhost: localhost\nport: 5432\nEOF"),
        ("find-exec-batch", "`find -exec +` batches arguments like xargs for fewer process spawns.", "find . -name '*.log' -exec gzip {} +"),
    ],
    "database": [
        ("explain-analyze", "`EXPLAIN ANALYZE` shows actual execution time and row counts, not just estimates.", "EXPLAIN ANALYZE\nSELECT * FROM users WHERE age > 25"),
        ("partial-index", "Partial indexes only index rows matching a condition, saving space and write overhead.", "CREATE INDEX idx_active ON users(email)\nWHERE active = true"),
        ("recursive-cte", "Recursive CTEs traverse tree/graph structures in a single query.", "WITH RECURSIVE tree AS (\n  SELECT id, parent_id, 1 AS depth\n  FROM nodes WHERE parent_id IS NULL\n  UNION ALL\n  SELECT n.id, n.parent_id, t.depth + 1\n  FROM nodes n JOIN tree t ON n.parent_id = t.id\n)\nSELECT * FROM tree"),
        ("upsert-on-conflict", "`INSERT ON CONFLICT` handles upserts atomically in PostgreSQL.", "INSERT INTO kv(key, val) VALUES('a', 1)\nON CONFLICT(key) DO UPDATE SET val = EXCLUDED.val"),
        ("lateral-join", "`LATERAL` joins let subqueries reference earlier tables in FROM clause.", "SELECT u.name, t.title\nFROM users u,\nLATERAL (\n  SELECT title FROM tasks\n  WHERE user_id = u.id\n  ORDER BY created_at DESC LIMIT 3\n) t"),
        ("window-functions", "Window functions compute values across related rows without collapsing them.", "SELECT name, salary,\n  RANK() OVER (PARTITION BY dept ORDER BY salary DESC)\nFROM employees"),
    ],
    "devops": [
        ("twelve-factor-config", "Store config in environment variables, not in code or config files (12-factor app).", "DATABASE_URL=postgres://user:pass@host/db python app.py"),
        ("liveness-vs-readiness", "Liveness probes restart crashed containers. Readiness probes stop traffic to busy ones.", "livenessProbe:\n  httpGet:\n    path: /healthz\nreadinessProbe:\n  httpGet:\n    path: /ready"),
        ("blue-green-deploy", "Blue-green deploys run two identical environments and switch traffic atomically.", "# 1. Deploy to green (inactive)\n# 2. Run smoke tests on green\n# 3. Switch LB to green\n# 4. Blue becomes inactive"),
        ("gitops-pull-model", "GitOps pull model: the cluster watches the repo, CI never touches the cluster.", "# ArgoCD detects drift between git state and cluster state\n# Auto-syncs or alerts based on policy"),
        ("canary-deploy", "Canary deployments route a small percentage of traffic to the new version first.", "# 5% traffic -> v2\n# Monitor error rate\n# If OK, ramp to 25% -> 50% -> 100%"),
    ],
    "api": [
        ("idempotency-key", "Idempotency keys prevent duplicate operations on retry.", "POST /payments\nIdempotency-Key: abc-123-unique"),
        ("cursor-pagination", "Cursor pagination is more stable than offset for real-time data feeds.", "GET /items?cursor=eyJpZCI6MTAwfQ&limit=20"),
        ("rate-limit-headers", "Standard rate limit headers help clients self-throttle before hitting limits.", "X-RateLimit-Limit: 100\nX-RateLimit-Remaining: 42\nX-RateLimit-Reset: 1620000000"),
        ("etag-caching", "`ETag` + `If-None-Match` enables conditional requests and 304 responses.", 'Response: ETag: "33a64df5"\nRequest: If-None-Match: "33a64df5"\nResponse: 304 Not Modified'),
        ("hateoas-links", "HATEOAS provides navigable links in API responses for discoverability.", '{\n  "id": 1,\n  "_links": {\n    "self": "/users/1",\n    "orders": "/users/1/orders"\n  }\n}'),
    ],
    "testing": [
        ("arrange-act-assert", "AAA pattern structures tests into setup, execution, and verification.", "# Arrange\nuser = create_user(name='test')\n# Act\nresult = user.login('password')\n# Assert\nassert result.success is True"),
        ("fixture-scope", "pytest fixtures with `scope='module'` run once per module, not per test.", "@pytest.fixture(scope='module')\ndef db():\n    return setup_test_db()"),
        ("snapshot-testing", "Snapshot tests capture output and compare against a saved baseline.", "expect(render(<Button />)).toMatchSnapshot()"),
        ("property-based-testing", "Property-based tests generate random inputs to find edge cases.", "@given(st.lists(st.integers()))\ndef test_sort_idempotent(xs):\n    assert sorted(sorted(xs)) == sorted(xs)"),
        ("test-doubles", "Stubs return canned answers. Mocks verify interactions. Fakes have working implementations.", "# Stub: always returns 200\n# Mock: asserts .send() was called once\n# Fake: in-memory DB with real queries"),
    ],
}


def generate_date_schedule(start: datetime, end: datetime) -> list[tuple[datetime, int]]:
    """Generate a natural-looking schedule of (date, num_commits) pairs."""
    schedule = []
    current = start
    while current <= end:
        weekday = current.weekday()  # 0=Mon, 6=Sun
        rand = random.random()

        # Probability of committing
        if weekday < 5:  # Mon-Fri
            prob = 0.62
        elif weekday == 5:  # Sat
            prob = 0.15
        else:  # Sun
            prob = 0.08

        if rand < prob:
            # Number of commits: weighted toward 1-3, occasionally 4-7
            weights = [30, 25, 20, 12, 7, 4, 2]  # 1-7 commits
            num = random.choices(range(1, 8), weights=weights, k=1)[0]

            # Tue-Thu slightly more active
            if weekday in (1, 2, 3):
                num = min(num + random.choice([0, 0, 1]), 7)

            schedule.append((current, num))

        current += timedelta(days=1)

    return schedule


def pick_til(used: set) -> tuple[str, str, str, str] | None:
    """Pick a random unused TIL. Returns (category, slug, desc, code) or None."""
    all_tils = []
    for cat, items in TILS.items():
        for slug, desc, code in items:
            key = f"{cat}/{slug}"
            if key not in used:
                all_tils.append((cat, slug, desc, code))
    if not all_tils:
        return None
    return random.choice(all_tils)


def make_commit_time(date: datetime, commit_idx: int) -> str:
    """Generate a realistic commit timestamp for the given date."""
    # Work hours distribution: 9-18 with peak at 10-15
    if random.random() < 0.8:
        hour = random.choices(
            range(9, 19),
            weights=[5, 15, 12, 10, 15, 12, 8, 5, 3, 2],
            k=1
        )[0]
    else:
        hour = random.choice([8, 19, 20, 21])

    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    dt = date.replace(hour=hour, minute=minute, second=second)
    # KST = UTC+9
    return dt.strftime("%Y-%m-%dT%H:%M:%S+09:00")


def run(cmd: str, env_override: dict | None = None):
    env = os.environ.copy()
    if env_override:
        env.update(env_override)
    subprocess.run(cmd, shell=True, check=True, capture_output=True, env=env)


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    end = datetime(2026, 4, 15)
    start = datetime(2025, 4, 16)

    schedule = generate_date_schedule(start, end)
    used_tils = set()
    total_commits = 0

    print(f"Schedule: {len(schedule)} active days, ~{sum(n for _, n in schedule)} commits")

    commit_messages = [
        "add til: {cat}/{slug}",
        "learn: {title}",
        "note: {title}",
        "til: {title}",
        "add {cat} note: {title}",
    ]

    for day_idx, (date, num_commits) in enumerate(schedule):
        for ci in range(num_commits):
            til = pick_til(used_tils)
            if til is None:
                # All TILs used — create minor update commits
                cat = random.choice(list(TILS.keys()))
                filepath = f"{cat}/.notes"
                with open(filepath, "a") as f:
                    f.write(f"ref {date.strftime('%Y-%m-%d')} #{ci}\n")
                timestamp = make_commit_time(date, ci)
                run(f'git add "{filepath}"')
                date_env = {"GIT_AUTHOR_DATE": timestamp, "GIT_COMMITTER_DATE": timestamp}
                run(f'git commit -m "update {cat} notes"', env_override=date_env)
                total_commits += 1
                continue

            cat, slug, desc, code = til
            used_tils.add(f"{cat}/{slug}")

            title = slug.replace("-", " ")
            filepath = f"{cat}/{slug}.md"

            # Create TIL file
            content = f"""# {title}

{desc}

```
{code}
```

_Learned on {date.strftime('%Y-%m-%d')}_
"""
            os.makedirs(cat, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            # Commit with backdated timestamp
            timestamp = make_commit_time(date, ci)
            run(f'git add "{filepath}"')

            msg = random.choice(commit_messages).format(cat=cat, slug=slug, title=title)
            date_env = {"GIT_AUTHOR_DATE": timestamp, "GIT_COMMITTER_DATE": timestamp}
            run(f'git commit -m "{msg}"', env_override=date_env)
            total_commits += 1

        if (day_idx + 1) % 30 == 0:
            print(f"  Progress: {day_idx+1}/{len(schedule)} days, {total_commits} commits")

    print(f"\nDone! Total: {total_commits} commits across {len(schedule)} days")
    print(f"Used {len(used_tils)}/{sum(len(v) for v in TILS.values())} unique TIL topics")
    print("Now run: git push origin main")


if __name__ == "__main__":
    main()
