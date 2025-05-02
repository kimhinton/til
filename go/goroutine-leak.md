# goroutine leak

Always ensure goroutines can exit. Use context cancellation or done channels.

```
go func() {
    select {
    case <-done:
        return
    case ch <- val:
    }
}()
```

_Learned on 2025-05-02_
