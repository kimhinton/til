# table driven tests

Table-driven tests use a slice of test cases for exhaustive coverage.

```
tests := []struct {
    input string
    want  int
}{
    {"hello", 5},
    {"", 0},
}
```

_Learned on 2025-04-18_
