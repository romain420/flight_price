FROM python:3.9

RUN mkdir /usr/src/workspace
WORKDIR /usr/src/workspace

COPY ./requirements.txt .
RUN pip install -r requirements.txt