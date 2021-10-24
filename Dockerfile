FROM python:3.6-alpine

COPY ./src app

COPY ./src/requirements.txt /app/requirements.txt

WORKDIR app

EXPOSE 5050:5000

RUN pip install -r requirements.txt

CMD [ "python", "mail_sender.py" ]