# у нас дизмараль, мультисборки не будет и пользака тоже не будет!
FROM node:21-alpine3.18 as frontend

WORKDIR /app
COPY ./chackaton ./

RUN npm i && npm run build

FROM nginx:1.25.4-alpine
COPY --from=frontend /app/dist/spa /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf:ro
COPY configs/site.conf /etc/nginx/conf.d/site.conf:ro