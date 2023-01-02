# pull official base image
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /home/dabl

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev gcc build-essential zlib1g-dev libjpeg-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements requirements
RUN pip install -r requirements/docker.txt

# copy project
COPY app app
COPY migrations migrations
COPY dabl.py config.py boot.sh ./

# set permissions and execute shell script to start
RUN ["chmod", "+x", "boot.sh"]
ENTRYPOINT ["sh", "./boot.sh"]