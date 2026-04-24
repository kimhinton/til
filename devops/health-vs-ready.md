# health vs ready

Liveness probes restart; readiness probes stop traffic. Different purposes.

```
livenessProbe:\n  httpGet: {path: /healthz}\nreadinessProbe:\n  httpGet: {path: /ready}
```

_Learned on 2026-04-24_
<!-- ref 13342 -->
