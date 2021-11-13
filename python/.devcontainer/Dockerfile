FROM python:3.10.0-alpine
WORKDIR /usr/app
COPY . /usr/app
RUN apk update && apk upgrade && apk add bash \
    && python setup.py install \
    && rm -rf /usr/app