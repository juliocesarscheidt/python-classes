import os
import json
from datetime import datetime


def lambda_handler(event, context):
    print("event", event)
    print("context", context)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00")
    print("now", now)
    message = os.environ.get("MESSAGE", "Hello World")
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": str(message + " " + now),
                "resource": event["resource"],
                "path": event["path"],
                "method": event["httpMethod"],
                "resource": event["resource"],
            }
        ),
    }
