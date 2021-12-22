FROM node:17-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install && npm build

FROM nginx:alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/build .
ENTRYPOINT ["nginx", "-g", "daemon off;"]