FROM python:3.8
ENV TZ="Europe/Berlin"
# Install cron
RUN apt update && apt -y install cron

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile

#Copy python files
COPY ./*.py .
COPY ./.env ./.env

WORKDIR /usr/app/Divera
COPY ./Divera/*.py .

WORKDIR /usr/app/Hermine
COPY ./Hermine/*.py .

WORKDIR /usr/app

CMD ["cron", "-f"]
