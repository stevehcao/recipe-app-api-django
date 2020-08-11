FROM python:3.7-alpine
LABEL maintainer="steve.cao.orders@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# no cache to minimize footprint of docker
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    # deps for alpine image, found on google for dependencies
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# delete temp
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user