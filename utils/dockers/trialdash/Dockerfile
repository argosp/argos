FROM node:12.18.4-alpine
ENV APP_DIR /usr/src/app/
WORKDIR $APP_DIR

COPY ./trialdash/package*.json ./trialdash/yarn.lock $APP_DIR
RUN yarn install

RUN yarn upgrade
COPY ./trialdash $APP_DIR
RUN yarn add @babel/helper-call-delegate
RUN yarn build