FROM python:3.10.0-alpine
WORKDIR /usr/app
COPY . /usr/app

ENV PYTHON_PKG_FOLDER_NAME "package"
ENV PYTHON_PKG_TEST_FOLDER_NAME "tests"

RUN apk update && apk upgrade && apk add bash \
    && pip install . \
    && rm -rf /usr/app