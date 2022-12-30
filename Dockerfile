FROM python:3.7.4-buster

ENV FLASK_APP dabl.py
ENV FLASK_CONFIG production

RUN adduser dabl
USER dabl

WORKDIR /home/dabl

COPY requirements requirements
ENV PATH=/home/dabl/.virtualenvs/bin:$PATH

#RUN venv/bin/pip3 install -r requirements/docker.txt
RUN pip3 install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY dabl.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]