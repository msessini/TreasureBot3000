#running with tensorflow will be more efficient than with python
FROM tensorflow/tensorflow:2.10.0
# WORKDIR /prod
#FROM python:3.10.6-buster
COPY requirements.txt requirements.txt
# to reduce the unnecessary packages
RUN pip install -r requirements.txt
COPY treasurebot treasurebot
COPY setup.py setup.py
RUN pip install .
CMD uvicorn treasurebot.api.main:app --host 0.0.0.0 --port $PORT
