# error wrapping

Use `fmt.Errorf` with `%w` to wrap errors for `errors.Is/As` unwrapping.

```
return fmt.Errorf("query failed: %w", err)
```

_Learned on 2025-05-06_
