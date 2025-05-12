# find exec batch

`find -exec +` batches arguments like xargs for fewer process spawns.

```
find . -name '*.log' -exec gzip {} +
```

_Learned on 2025-05-12_
