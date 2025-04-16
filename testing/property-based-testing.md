# property based testing

Property-based tests generate random inputs to find edge cases.

```
@given(st.lists(st.integers()))
def test_sort_idempotent(xs):
    assert sorted(sorted(xs)) == sorted(xs)
```

_Learned on 2025-04-16_
