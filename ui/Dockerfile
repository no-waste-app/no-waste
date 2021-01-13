 # build environment
FROM node:14.15-alpine as build

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock
RUN yarn install

COPY . /app
RUN yarn run build

# runtime environment
FROM nginx:1.19.6-alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8000
CMD ["nginx", "-g", "daemon off;"]