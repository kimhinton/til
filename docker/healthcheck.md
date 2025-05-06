# healthcheck

`HEALTHCHECK` instruction tells Docker how to test container health.

```
HEALTHCHECK --interval=30s CMD curl -f http://localhost/ || exit 1
```

_Learned on 2025-05-06_
