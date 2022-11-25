FROM node:16-alpine AS build

WORKDIR /app

COPY package.json ./

COPY package-lock.json ./

RUN npm install

COPY . ./

EXPOSE 8080

CMD ["npm", "run", "dev"]
