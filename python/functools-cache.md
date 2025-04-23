# functools cache

`@functools.cache` provides unlimited memoization. Use `@lru_cache(maxsize=N)` for bounded cache.

```
@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

_Learned on 2025-04-23_
