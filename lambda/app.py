

def main_lambda(event):
    print("main_lambda")
    return {"status": "ok"}


def handler(event, context):
    """
    AWS Lambda handler
    """
    print(event)
    res = main_lambda(event)
    print("===")
    return res
