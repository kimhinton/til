# typing protocol

`typing.Protocol` enables structural subtyping (duck typing with type hints).

```
class Drawable(Protocol):
    def draw(self) -> None: ...
```

_Learned on 2025-05-20_
