# multi stage build

Multi-stage builds reduce final image size by copying only artifacts.

```
FROM node:20 AS build
RUN npm run build
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

_Learned on 2025-04-30_
