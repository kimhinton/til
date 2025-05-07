# structural pattern matching

Python 3.10 `match/case` supports structural pattern matching with guards.

```
match command:
    case ['go', direction] if direction in VALID:
        move(direction)
    case _:
        print('unknown')
```

_Learned on 2025-05-07_
