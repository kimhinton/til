# asyncio gather

`asyncio.gather` runs multiple coroutines concurrently and collects results.

```
results = await asyncio.gather(
    fetch(url1),
    fetch(url2),
    fetch(url3)
)
```

_Learned on 2025-04-24_
