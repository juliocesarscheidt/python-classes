import os
# pip install -r requirements.txt
import sqlite3
import logging
import tempfile
from markupsafe import escape
from threading import Lock, current_thread
from datetime import datetime
from flask_httpauth import HTTPTokenAuth
from flask import Flask, make_response, jsonify, request

# set logging
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)
logger = logging.getLogger()

# get temp directory
temp_dir = tempfile.gettempdir()
DB_PATH = temp_dir + "/database.db"
logger.info({"DB_PATH": DB_PATH})

# global vars
API_SECRET_TOKEN = os.environ.get('API_SECRET_TOKEN',
                                  'r9GwP4WRj8GKlhFNLJUyxjVN6ReRysY5wbNBGtTS944bBKk8Z6erVJ4HyQnu1X8u')
logger.info({"API_SECRET_TOKEN": API_SECRET_TOKEN})

# open sqlite connection
conn = sqlite3.connect(DB_PATH, check_same_thread=False)

def migrate(conn):
  MESSAGE = os.environ.get('MESSAGE', 'Hello World')
  MESSAGE = str(escape(MESSAGE)).strip()
  logger.info({"MESSAGE": MESSAGE})
  # retrieve a cursor
  cursor = conn.cursor()
  # create table
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS configuration (
    name VARCHAR(255) NOT NULL PRIMARY KEY,
    content VARCHAR(255) NOT NULL
  );
  """)
  conn.commit() # transactional must commit
  # upsert
  cursor.execute("""
  INSERT OR REPLACE INTO configuration(name, content)
  VALUES(
    ?,
    COALESCE((SELECT content FROM configuration WHERE name = ?), ?)
  );
  """, ["message", "message", MESSAGE])
  conn.commit() # transactional must commit
  # sqlite upsert draw - version 3.24.0 # https://www.sqlite.org/draft/lang_UPSERT.html
  # INSERT INTO configuration(name, content)
  #   VALUES (?, ?)
  # ON
  #   CONFLICT(name) DO NOTHING;
  cursor.close()

# run migrations
migrate(conn)

# create flask app
app = Flask(__name__)
auth = HTTPTokenAuth('Token')

def get_datetime_now():
  return datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000+00:00')

@auth.verify_token
def verify_token(token):
  return token == API_SECRET_TOKEN

@auth.error_handler
def unauthorized(status_code):
  response = jsonify(status='Error', message='Unauthorized')
  return make_response(response, status_code)

@app.route('/message', methods=['GET'])
@auth.login_required
def index():
  logger.info({"MESSAGE THREAD": current_thread().ident})

  # retrieve a cursor
  cursor = conn.cursor()
  message = cursor.execute("SELECT content FROM configuration WHERE name = ?", ['message']).fetchone()[0]
  cursor.close()

  response = jsonify(status='Success', message=message,
                     datetime=get_datetime_now(), path=request.path, method=request.method)
  return make_response(response, 200)

@app.route('/configuration', methods=['POST'])
@auth.login_required
def configuration():
  logger.info({"CONFIGURATION THREAD": current_thread().ident})
  message = request.json['message'] if 'message' in request.json else None
  if message is None or message == "":
    response = jsonify(status='Error', message='Bad Request')
    return make_response(response, 400)
  message = str(escape(message)).strip()

  lock = Lock()
  lock.acquire()

  # retrieve a cursor
  cursor = conn.cursor()
  cursor.execute("UPDATE configuration SET content = ? WHERE name = ?", [message, 'message'])
  conn.commit() # transactional must commit
  cursor.close()

  lock.release()
  response = jsonify(status='Accepted', message=message,
                     datetime=get_datetime_now(), path=request.path, method=request.method)
  return make_response(response, 202)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9000)
