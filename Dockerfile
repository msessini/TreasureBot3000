#FROM tensorflow/tensorflow:2.10.0
FROM python:3.10.6-buster
#WORKDIR /prod
RUN apt-get update && apt-get install libgl1 -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY treasurebot treasurebot
COPY setup.py setup.py
COPY treasurebot3000-serviceaccount.json treasurebot3000-serviceaccount.json
RUN pip install .
CMD uvicorn treasurebot.api.main:app --host 0.0.0.0 --port $PORT
