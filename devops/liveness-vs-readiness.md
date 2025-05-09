# liveness vs readiness

Liveness probes restart crashed containers. Readiness probes stop traffic to busy ones.

```
livenessProbe:
  httpGet:
    path: /healthz
readinessProbe:
  httpGet:
    path: /ready
```

_Learned on 2025-05-09_
