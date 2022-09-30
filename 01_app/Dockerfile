FROM node:alpine3.15 
RUN npm install -g npm@8.11.0
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
USER 1000
COPY . .
EXPOSE 8080
CMD [ "node", "app.js" ]

