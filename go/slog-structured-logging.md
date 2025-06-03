# slog structured logging

`log/slog` provides structured logging with key-value pairs (Go 1.21+).

```
slog.Info("request",
    "method", r.Method,
    "path", r.URL.Path,
)
```

_Learned on 2025-06-03_
