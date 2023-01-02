FROM python:3.7.4-buster

ENV FLASK_APP dabl.py
ENV FLASK_CONFIG production

RUN adduser dabl
#USER dabl

WORKDIR /home/dabl

COPY requirements requirements

RUN pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY dabl.py config.py ./

RUN ["chmod", "+x", "boot.sh"]

EXPOSE 5000

#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
ENTRYPOINT ["sh", "./boot.sh"]