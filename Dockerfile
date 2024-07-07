FROM python:3.8
ENV TZ="Europe/Berlin"

RUN apt update && apt -y install cron

ADD cronfile /etc/cron.d/
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile

WORKDIR /usr/app/

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

#Copy python files
ADD ./*.py ./
ADD ./.env ./


ADD ./Divera/*.py Divera/

ADD ./Hermine/*.py Hermine/

WORKDIR /usr/app/

CMD ["cron", "-f"]
