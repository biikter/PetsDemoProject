import json
import jsonschema
from jsonschema import validate

class Json_Utils():
    @staticmethod
    def validateJson(jsonData, schema):
        try:
            validate(instance=jsonData, schema=schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True