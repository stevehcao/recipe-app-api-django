FROM python:3.7-alpine
LABEL maintainer="steve.cao.orders@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# no cache to minimize footprint of docker
# won't be removed
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    # deps for alpine image, found on google for dependencies
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
# delete temp
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

###
# these create two new dir to store media and static
# webserver container might need to know these vols
# -p flag will create directory that do not exist in path, 
# ex. if vol doesn't exist it will create for us
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
# chown will set ownership to user, -R is recursive
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
###




