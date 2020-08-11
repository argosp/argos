FROM node:10.15
ENV APP_DIR /usr/src/app/
WORKDIR $APP_DIR

COPY ./trialgraph/package*.json ./trialgraph/package-lock.lock $APP_DIR
RUN npm install
COPY . .