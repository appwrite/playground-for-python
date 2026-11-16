FROM python:3.10-alpine@sha256:8ca9f9d0f4df2af674092e7e9d79ce7985e783cecfe070f8ea850801b6520bf7
WORKDIR /app
RUN apk update && apk add git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python playground.py
