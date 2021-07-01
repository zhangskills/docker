FROM python:3-slim

RUN pip install hanlp Flask uniout gevent

WORKDIR /usr/src/myapp

COPY ./main.py .

CMD [ "python", "main.py" ]