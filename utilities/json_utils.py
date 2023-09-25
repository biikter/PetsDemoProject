import json
import jsonschema
from jsonschema import validate


class JsonUtils:
    @staticmethod
    def validate_json(json_data, schema):
        try:
            validate(instance=json_data, schema=schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
