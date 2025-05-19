# blue green deploy

Blue-green deploys run two identical environments and switch traffic atomically.

```
# 1. Deploy to green (inactive)
# 2. Run smoke tests on green
# 3. Switch LB to green
# 4. Blue becomes inactive
```

_Learned on 2025-05-19_
