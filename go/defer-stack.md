# defer stack

Deferred calls execute LIFO (last in, first out). Useful for cleanup.

```
f, _ := os.Open(name)
defer f.Close()
```

_Learned on 2025-05-10_
