FROM node:16 AS builder
WORKDIR /app
COPY server.js /app
COPY package.json /app

RUN yarn && yarn run build && yarn cache clean


FROM nginx:alpine

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*

COPY --from=builder /app/build .

EXPOSE 80/tcp

ENTRYPOINT ["nginx", "-g", "daemon off;"]
