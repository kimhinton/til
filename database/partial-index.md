# partial index

Partial indexes only index rows matching a condition, saving space and write overhead.

```
CREATE INDEX idx_active ON users(email)
WHERE active = true
```

_Learned on 2025-04-30_
