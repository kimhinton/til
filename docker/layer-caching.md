# layer caching

Order Dockerfile instructions from least to most frequently changing for cache efficiency.

```
COPY package.json .
RUN npm install
COPY . .  # source changes don't bust npm cache
```

_Learned on 2025-05-26_
