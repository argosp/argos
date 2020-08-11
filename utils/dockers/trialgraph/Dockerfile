FROM node:10.15
ENV APP_DIR /usr/src/app/
WORKDIR $APP_DIR
COPY ./trialgraph/package*.json $APP_DIR
RUN npm install
RUN npm install -g nodemon

COPY ./trialgraph $APP_DIR