import logging
import json


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def lambda_handler(event, context):
    log.info("Received event: {}".format(json.dumps(event, indent=2)))
    body = {
        "message": "{} {}".format(event["greeting"], event["name"])
    }
    headers = {
        "Content-Type": "application/json"
    }
    result = {
        "statusCode": 200,
        "headers": headers,
        "body": body
    }
    return result
