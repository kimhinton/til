# fixture scope

pytest fixtures with `scope='module'` run once per module, not per test.

```
@pytest.fixture(scope='module')
def db():
    return setup_test_db()
```

_Learned on 2025-06-03_
