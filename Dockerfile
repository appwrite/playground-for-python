FROM python:3.11.11-alpine

WORKDIR /app
RUN apk update && apk add git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python playground.py
