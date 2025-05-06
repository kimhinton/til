# window functions

Window functions compute values across related rows without collapsing them.

```
SELECT name, salary,
  RANK() OVER (PARTITION BY dept ORDER BY salary DESC)
FROM employees
```

_Learned on 2025-05-06_
