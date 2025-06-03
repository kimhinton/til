# sync once

`sync.Once` ensures a function runs exactly once across goroutines.

```
var once sync.Once
once.Do(func() { db = connectDB() })
```

_Learned on 2025-06-03_
