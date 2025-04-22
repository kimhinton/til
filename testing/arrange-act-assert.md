# arrange act assert

AAA pattern structures tests into setup, execution, and verification.

```
# Arrange
user = create_user(name='test')
# Act
result = user.login('password')
# Assert
assert result.success is True
```

_Learned on 2025-04-23_
