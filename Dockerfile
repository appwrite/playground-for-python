FROM python:3.10-alpine
WORKDIR /app
RUN apk update && apk add git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python playground.py
