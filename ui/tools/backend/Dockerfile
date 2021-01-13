FROM node:14

# Create app directory
WORKDIR /app

COPY package.json ./
COPY yarn.lock ./

RUN yarn install

# Bundle app source
COPY . .
RUN yarn run build

EXPOSE 8080
CMD [ "node", "src/index.js" ]