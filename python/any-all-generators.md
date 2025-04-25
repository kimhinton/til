# any all generators

`any()` and `all()` short-circuit on generator expressions.

```
has_error = any(r.status >= 400 for r in responses)
```

_Learned on 2025-04-25_
