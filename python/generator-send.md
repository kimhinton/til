# generator send

`generator.send()` pushes a value into a paused generator at `yield`.

```
def accumulator():
    total = 0
    while True:
        total += yield total
```

_Learned on 2025-04-24_
