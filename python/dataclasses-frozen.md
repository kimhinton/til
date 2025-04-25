# dataclasses frozen

Use `@dataclass(frozen=True)` to create immutable instances. Raises `FrozenInstanceError` on attribute assignment.

```
@dataclass(frozen=True)
class Point:
    x: float
    y: float
```

_Learned on 2025-04-25_
