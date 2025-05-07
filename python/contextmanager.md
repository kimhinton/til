# contextmanager

`contextlib.contextmanager` turns a generator into a context manager. `yield` separates setup from teardown.

```
@contextmanager
def timer():
    start = time.time()
    yield
    print(f'{time.time()-start:.2f}s')
```

_Learned on 2025-05-07_
