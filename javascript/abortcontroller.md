# abortcontroller

`AbortController` cancels fetch requests and other async operations.

```
const ctrl = new AbortController()
fetch(url, { signal: ctrl.signal })
ctrl.abort()
```

_Learned on 2025-05-23_
