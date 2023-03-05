FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r \
    requirements.txt
COPY ./ ./

ENV FLASK_ENV="development"
EXPOSE 9000

CMD [ "python", "-u", "main.py" ]
