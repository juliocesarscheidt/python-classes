FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r \
    requirements.txt

COPY ./ ./

EXPOSE 9000

CMD [ "python", "-u", "main.py" ]
