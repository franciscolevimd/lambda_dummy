import json
import logging

from aws import lambda_function as aws


logging.basicConfig(filename='poke.log')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def main():
    result = aws.lambda_handler({"name": "pikachu"}, None)
    log.info(f"Received event:\n{json.dumps(result, indent=2)}")


if __name__ == '__main__':
    main()
