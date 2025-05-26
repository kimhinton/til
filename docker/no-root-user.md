# no root user

Run containers as non-root for security. Create a dedicated user.

```
RUN adduser -D appuser
USER appuser
```

_Learned on 2025-05-26_
