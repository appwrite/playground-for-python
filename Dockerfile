FROM python:3.15-alpine@sha256:0f9552bb28711333da16915ec146f5e6bb44a7fdac9ced15dc17c2e0206346dd
WORKDIR /app
RUN apk update && apk add git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python playground.py
