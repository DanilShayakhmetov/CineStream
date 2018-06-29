FROM node:10.5.0
WORKDIR /chat
COPY chat/package.json /chat
RUN npm install
COPY ./chat /chat
CMD node app.js
EXPOSE 8888

