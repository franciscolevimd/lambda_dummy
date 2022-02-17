import json
import logging

from zoehi import lambda_function as zoe


logging.basicConfig(filename="zoehi.log")
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def main():
    event = {
        "name": "Zoehi",
        "greeting": "Hola"
    }
    response = zoe.lambda_handler(event=event, context=None)
    log.info("Response:\n{}".format(json.dumps(response, indent=2)))

    
if __name__ == '__main__':
    main()
