from flask import Flask
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
  now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000+00:00')
  print("now", now)
  return json.dumps({
    "message": now,
  })

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9000)

# docker image build --tag juliocesarmidia/flask-sample:latest
# docker container run -d --rm --name flask-sample --publish 9000:9000 juliocesarmidia/flask-sample:latest
# docker container logs -f --tail 100 flask-sample
# curl --url http://localhost:9000/
