# slots dataclass

`__slots__` in dataclasses reduces memory footprint by preventing `__dict__` creation.

```
@dataclass(slots=True)
class Vector:
    x: float
    y: float
```

_Learned on 2025-04-24_
