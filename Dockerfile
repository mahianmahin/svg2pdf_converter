FROM python:3.8-alpine
RUN apk add --no-cache \
     build-base cairo-dev cairo cairo-tools bash

WORKDIR /usr/src/
COPY . /usr/src/

RUN pip install -r requirements.txt

CMD python3 svg-converter-service.py