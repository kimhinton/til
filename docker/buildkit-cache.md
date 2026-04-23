# buildkit cache

BuildKit cache mounts speed up package installation across builds.

```
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
```

_Learned on 2026-04-23_
