import os
import json

# pip install -r requirements.txt
import requests


def make_request(url, method="GET", token=None, data=None):
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
    }
    if token is not None:
        headers.update(
            {"Authorization": token, }
        )
    response = requests.request(method=method, json=data,
                                url=url, headers=headers)
    return response.json()


API_SECRET_TOKEN = os.environ.get(
    "API_SECRET_TOKEN",
    "r9GwP4WRj8GKlhFNLJUyxjVN6ReRysY5wbNBGtTS944bBKk8Z6erVJ4HyQnu1X8u",
)

if __name__ in "__main__":
    url = "http://localhost:9000"

    response = make_request(f"{url}/message", "GET",
                            f"Token {API_SECRET_TOKEN}", None)
    print(response)
    print(response["message"])
    # hello world

    # change message
    make_request(
        f"{url}/configuration",
        "POST",
        f"Token {API_SECRET_TOKEN}",
        {"message": "Flask API"},
    )

    response = make_request(f"{url}/message", "GET",
                            f"Token {API_SECRET_TOKEN}", None)
    print(response)
    print(response["message"])
    # Flask API
