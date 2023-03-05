import os
# pip install -r requirements.txt
from flask import Flask, make_response, jsonify, request, escape
from flask_httpauth import HTTPTokenAuth
from flask_restful import Resource

import json
from datetime import datetime

MESSAGE = os.environ.get('MESSAGE', 'Hello World')
print("MESSAGE", MESSAGE)

API_SECRET_TOKEN = os.environ.get('API_SECRET_TOKEN', 'r9GwP4WRj8GKlhFNLJUyxjVN6ReRysY5wbNBGtTS944bBKk8Z6erVJ4HyQnu1X8u')
print("API_SECRET_TOKEN", API_SECRET_TOKEN)

app = Flask(__name__)
auth = HTTPTokenAuth('Token')

@auth.verify_token
def verify_token(token):
  print("token", token)
  return token == API_SECRET_TOKEN

@auth.error_handler
def unauthorized(status_code):
  print("status_code", status_code)
  response = jsonify(status='Error', message='Unauthorized')
  return make_response(response, status_code)

@app.route('/', methods=['GET'])
@auth.login_required
def index():
  now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000+00:00')
  print("now", now)
  response = jsonify(status='Success', message=MESSAGE, datetime=now, path=request.path, method=request.method)
  return make_response(response, 200)

@app.route('/configuration', methods=['POST'])
@auth.login_required
def configuration():
  message = request.form['message']
  message = str(escape(message)).strip()
  print("message", message)
  if message is None or message == "":
    response = jsonify(status='Error', message='Bad Request')
    return make_response(response, 400)
  
  MESSAGE = message
  
  response = jsonify(status='Accepted', message="Accepted")
  return make_response(response, 202)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9000)

# docker image build --tag juliocesarmidia/flask-sample:latest
# docker container run -d --rm --name flask-sample --publish 9000:9000 juliocesarmidia/flask-sample:latest
# docker container logs -f --tail 100 flask-sample

# python -u main.py
# MESSAGE=Ok python -u main.py

# curl -i --url "http://localhost:9000/" -H "Authorization: Token r9GwP4WRj8GKlhFNLJUyxjVN6ReRysY5wbNBGtTS944bBKk8Z6erVJ4HyQnu1X8u"
# curl -i --url "http://localhost:9000/configuration" -X POST --data '{"message": "Ok"}' -H "Authorization: Token r9GwP4WRj8GKlhFNLJUyxjVN6ReRysY5wbNBGtTS944bBKk8Z6erVJ4HyQnu1X8u"
