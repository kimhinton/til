# xargs parallel

`xargs -P` runs commands in parallel across multiple CPU cores.

```
find . -name '*.jpg' | xargs -P4 -I{} convert {} -resize 50% {}
```

_Learned on 2025-04-17_
