# compose profiles

Docker Compose profiles selectively start services for different environments.

```
services:
  debug:
    profiles: [debug]
    image: busybox
```

_Learned on 2025-05-20_
