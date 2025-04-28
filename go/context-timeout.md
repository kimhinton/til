# context timeout

`context.WithTimeout` cancels downstream work after a deadline.

```
ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
defer cancel()
```

_Learned on 2025-04-28_
