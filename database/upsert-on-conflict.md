# upsert on conflict

`INSERT ON CONFLICT` handles upserts atomically in PostgreSQL.

```
INSERT INTO kv(key, val) VALUES('a', 1)
ON CONFLICT(key) DO UPDATE SET val = EXCLUDED.val
```

_Learned on 2025-04-18_
