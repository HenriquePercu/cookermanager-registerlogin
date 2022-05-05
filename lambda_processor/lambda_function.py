import json
from model.user import User

# import requests


def lambda_handler(event, context):
    body = json.loads(event.get("body"))
    print(body)
    print(body.get("name"))

    registering_user = User(12,
                            body['name'],
                            body['password'],
                            body['email'],
                            body['phone'],
                            "",
                            "")
    #create_user_login(registering_user)
    print(registering_user)
    # convert to dataclass

    # call create user login

    return {
        "statusCode": 200,
        "body": json.dumps(registering_user.__dict__)
    }
