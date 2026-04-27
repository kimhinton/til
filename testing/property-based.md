# property based

Property-based tests generate random inputs to find edge cases.

```
@given(st.lists(st.integers()))\ndef test_sort(xs): assert sorted(sorted(xs)) == sorted(xs)
```

_Learned on 2026-04-27_
