# etag caching

`ETag` + `If-None-Match` enables conditional requests and 304 responses.

```
Response: ETag: "33a64df5"
Request: If-None-Match: "33a64df5"
Response: 304 Not Modified
```

_Learned on 2025-05-23_
