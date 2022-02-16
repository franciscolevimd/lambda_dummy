import json
import logging

from pokemon import lambda_function as pok


logging.basicConfig(filename='poke.log')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def main():
    result = pok.lambda_handler({"name": "pikachu"}, None)
    log.info(f"Received event:\n{json.dumps(result, indent=2)}")


if __name__ == '__main__':
    main()
