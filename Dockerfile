#running with tensorflow will be more efficient than with python
#FROM tensorflow/tensorflow:2.10.0
FROM python:3.10.6-buster
#WORKDIR /prod
# to reduce the unnecessary packages
RUN apt-get update && apt-get install libgl1 -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY treasurebot treasurebot
COPY setup.py setup.py
COPY pictures pictures
COPY treasurebot-serviceaccount.json treasurebot-serviceaccount.json
RUN pip install .
CMD uvicorn treasurebot.api.main:app --host 0.0.0.0 --port $PORT
