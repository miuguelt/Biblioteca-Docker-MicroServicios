FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y libgtk-3-0

RUN mkdir -p /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    linux-headers-generic \
    gcc \
    libc6-dev

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "sleep", "infinity" ]
