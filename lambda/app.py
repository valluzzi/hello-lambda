import json

def main_lambda(event):
    """
    main loop
    """
    print("main_lambda")
    #body = event if event else {"status":"No event"}
    return {
        "statusCode": 200,
        "body": "Hello World!"
    }

def handler(event, context):
    """
    AWS Lambda handler
    """
    return main_lambda(event)
