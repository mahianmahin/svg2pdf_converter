FROM python:3.8-alpine
RUN apk add --no-cache \
     build-base cairo-dev cairo cairo-tools bash
RUN mkdir app
WORKDIR /app
COPY . /app

RUN mkdir -p /usr/share/fonts/
RUN python3 install_fonts.py

RUN pip install -r requirements.txt
CMD python3 svg-converter-service.py