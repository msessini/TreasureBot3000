FROM python:3.10.6-buster
COPY treasurebot3000/treasurebot3000
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn treasurebot3000.api.fast:app --host 0.0.0.0 --port $PORT
