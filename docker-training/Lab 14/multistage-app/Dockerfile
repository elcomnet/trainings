# Stage1 - Buil App

FROM node:10.0 AS builder

WORKDIR /build

COPY easyclaim-frontend .

RUN npm install \
    && npm run build

# Stage2 - Run app
FROM nginx:alpine

COPY --from=builder /build/dist/my-dream-app /usr/share/nginx/html

EXPOSE 80/tcp

ENTRYPOINT ["nginx", "-g", "daemon off;"]
