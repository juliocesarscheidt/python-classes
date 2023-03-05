
```bash
export API_SECRET_TOKEN="r9GwP4WRj8GKlhFNLJUyxjVN6ReRysY5wbNBGtTS944bBKk8Z6erVJ4HyQnu1X8u"
export MESSAGE="Hello World"
```

```bash
docker image build --tag juliocesarmidia/flask-sample:latest .

docker container run --rm -d \
  --name flask-sample \
  --env API_SECRET_TOKEN \
  --env MESSAGE \
  --publish 9000:9000 \
  --volume $PWD/tmp:/tmp \
  juliocesarmidia/flask-sample:latest

docker container run --rm -d \
  --name flask-sample \
  --env API_SECRET_TOKEN \
  --env MESSAGE \
  --env FLASK_ENV="production" \
  --publish 9000:9000 \
  --volume $PWD/tmp:/tmp \
  juliocesarmidia/flask-sample:latest \
  gunicorn -w 4 -b 0.0.0.0:9000 'main:app'

docker container logs -f --tail 100 flask-sample

docker container rm -f flask-sample
```

```bash
pip install -r requirements.txt

export FLASK_ENV="development"
python -u main.py

export FLASK_ENV="production"
gunicorn -w $(nproc) -b 0.0.0.0:9000 'main:app'
gunicorn -w 4 -b 0.0.0.0:9000 'main:app'

curl --url 'http://localhost:9000/message' \
  -H 'Content-type: application/json' \
  -H "Authorization: Token $API_SECRET_TOKEN"

curl --url 'http://localhost:9000/configuration' -X POST \
  --data '{"message": "Ok"}' \
  -H 'Content-type: application/json' \
  -H "Authorization: Token $API_SECRET_TOKEN"
```
