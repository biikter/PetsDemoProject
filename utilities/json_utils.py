import json
import jsonschema
from jsonschema import validate
import logging


class JsonUtils:
    @staticmethod
    def validate_json(json_data, schema):
        logging.getLogger().info("Validating JSON schema")
        try:
            validate(instance=json_data, schema=schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
