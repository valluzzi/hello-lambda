import json
from collections import defaultdict


def get_params(event):
    """
    get query params from GET or POST requests
    """
    print(type(event))
    if "body" in event and event["body"] is not None:
        event = json.loads(event["body"])
    elif "queryStringParameters" in event:
        event = event["queryStringParameters"]
    return defaultdict


def main_lambda(event):
    """
    main loop
    """
    params = get_params(event)

    name = params["name"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": f"hello {name}"
    }


def handler(event, context):
    """
    AWS Lambda handler
    """
    return main_lambda(event)
