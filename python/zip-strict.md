# zip strict

`zip(..., strict=True)` in Python 3.10+ raises ValueError on unequal lengths.

```
for a, b in zip(names, scores, strict=True):
    print(f'{a}: {b}')
```

_Learned on 2025-05-07_
