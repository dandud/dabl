FROM python:3.6-slim-stretch

ENV FLASK_APP dabl.py
ENV FLASK_CONFIG production

RUN adduser -D dabl
USER dabl

WORKDIR /home/dabl

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY dabl.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]