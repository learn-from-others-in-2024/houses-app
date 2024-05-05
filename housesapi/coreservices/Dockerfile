FROM python:latest

ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore
ENV FLASK_APP=core.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5005

WORKDIR /coreservices

COPY . /coreservices

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["flask", "run"]
