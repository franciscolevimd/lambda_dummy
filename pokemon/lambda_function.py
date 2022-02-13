import logging
import json
import requests


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def process_response(response, status_code):
    result = {"statusCode": status_code}
    if status_code == 200:
        body = {}
        body["id"] = response.get("id")
        body["name"] = response.get("name")
        body["abilities"] = response.get("abilities", [])
        body["types"] = response.get("types", [])
        result["body"] = body
    return result


def lambda_handler(event, context):
    log.info(f"Received event: {json.dumps(event, indent=2)}")
    value = event.get("name", None)
    if value is None:
        return {"statusCode": 404}
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{value}")
    return process_response(response.json(), response.status_code)
