import json
from mockrestserver.exceptions.custom import InvalidDataFormatError


def load_json(data):
    try:
        return json.loads(data)
    except json.ValueError as ex:
        InvalidDataFormatError(500, ex.message, "Check you JSON contents provided!")