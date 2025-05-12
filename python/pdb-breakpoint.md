# pdb breakpoint

`breakpoint()` is a built-in that replaces `import pdb; pdb.set_trace()`.

```
def process(data):
    breakpoint()  # drops into debugger
    return transform(data)
```

_Learned on 2025-05-12_
