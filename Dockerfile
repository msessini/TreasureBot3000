#running with tensorflow will be more efficient than with python
FROM tensorflow/tensorflow:2.10.0
#FROM python:3.10.6-buster
COPY requirements.txt requirements.txt
# to reduce the unnecessary packages
RUN pip install --no-cache-dir -r requirements.txt
COPY treasurebot treasurebot
CMD uvicorn treasurebot.api.fast:app --host 0.0.0.0 --port $PORT
