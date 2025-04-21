# buildkit cache mount

BuildKit cache mounts speed up package installation across builds.

```
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
```

_Learned on 2025-04-21_
