# recursive cte

Recursive CTEs traverse tree/graph structures in a single query.

```
WITH RECURSIVE tree AS (
  SELECT id, parent_id, 1 AS depth
  FROM nodes WHERE parent_id IS NULL
  UNION ALL
  SELECT n.id, n.parent_id, t.depth + 1
  FROM nodes n JOIN tree t ON n.parent_id = t.id
)
SELECT * FROM tree
```

_Learned on 2025-05-08_
