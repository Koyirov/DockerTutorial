FROM node

WORKDIR /web-app

COPY ./web-app/package.json .
RUN npm install

COPY ./web-app/app.js .

EXPOSE 8080

CMD ["node", "app.js"]
