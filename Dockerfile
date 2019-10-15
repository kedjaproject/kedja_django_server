FROM python:3.7
ENV PYTHONUNBUFFERED 1
# RUN apt-get update && apt-get -y install cron
RUN mkdir -p /app/src
RUN mkdir -p /app/var/log
WORKDIR /app/src
COPY requirements.txt /app/
RUN pip install -r ../requirements.txt
COPY src /app/src/
# Crontab scheduling
# COPY crontab /etc/cron.d/triart
# RUN crontab /etc/cron.d/triart
