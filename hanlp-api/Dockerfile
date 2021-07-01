FROM python:3-slim

RUN pip install hanlp Flask uniout gevent

WORKDIR /usr/src/myapp

COPY ./hanlp-api/main.py .

CMD [ "python", "main.py" ]