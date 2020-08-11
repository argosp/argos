FROM node:10.15
ENV APP_DIR /usr/src/app/
WORKDIR $APP_DIR

COPY ./trialdash/package*.json ./trialdash/yarn.lock $APP_DIR
RUN yarn install

COPY ./trialdash $APP_DIR
RUN yarn build