FROM python:latest

ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /coreservices

COPY . /coreservices

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
