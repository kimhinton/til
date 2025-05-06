# channels direction

Directional channels enforce send-only or receive-only at compile time.

```
func producer(ch chan<- int) {
    ch <- 42
}
```

_Learned on 2025-05-06_
