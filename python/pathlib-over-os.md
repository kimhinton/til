# pathlib over os

`pathlib.Path` is more readable than `os.path` for file operations.

```
path = Path('data') / 'file.csv'
content = path.read_text()
```

_Learned on 2025-05-02_
