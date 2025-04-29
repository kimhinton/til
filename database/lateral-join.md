# lateral join

`LATERAL` joins let subqueries reference earlier tables in FROM clause.

```
SELECT u.name, t.title
FROM users u,
LATERAL (
  SELECT title FROM tasks
  WHERE user_id = u.id
  ORDER BY created_at DESC LIMIT 3
) t
```

_Learned on 2025-04-29_
