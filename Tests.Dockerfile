FROM python:3.11.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/app
RUN apk update
RUN pip install --upgrade pip

# project dependencies
COPY ./requirements_test.txt .
RUN pip install -r requirements_test.txt

RUN mkdir -p /home/tests
RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/tests

COPY --chown=app:app ./tests $HOME
WORKDIR $HOME
USER app