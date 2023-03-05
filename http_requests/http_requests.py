import json
import os
# pip install requests
import requests

SVC_NAME = os.environ.get('SVC_NAME')
ENV_NAME = os.environ.get('ENV_NAME')
NAMESPACE = os.environ.get('NAMESPACE')
SVC_PORT = os.environ.get('SVC_PORT', 4080)

API_TOKEN = os.environ.get('API_TOKEN', '')

def make_request(url, method='GET', data=None):
  auth = None
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
  }
  headers.update({
    'Authorization': 'Bearer ' + API_TOKEN,
  })
  response = requests.request(method=method, json=data, url=url, headers=headers, auth=auth)
  return response.json()


url = 'http://kong-proxy/services'
make_request(url, 'POST', payload)

services = make_request(url, 'GET')

