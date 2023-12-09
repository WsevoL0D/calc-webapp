FROM python:3.11.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/app
RUN apk update
RUN pip install --upgrade pip

# project dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

COPY --chown=app:app ./calc_app $APP_HOME
WORKDIR $APP_HOME
USER app

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080"]