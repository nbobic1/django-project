FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y git postgresql build-essential libpq-dev

COPY ./requirements /requirements

COPY ./compose/local/docker-entrypoint /docker-entrypoint
RUN sed -i 's/\r//' /docker-entrypoint
RUN chmod +x /docker-entrypoint

RUN pip install -r /requirements/base.txt

WORKDIR /app
