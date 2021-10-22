FROM python:3.6.1-alpine

WORKDIR /src

ADD . /src

RUN pip install -r src/requirements.txt

CMD ["python","src/mail_sender.py"]