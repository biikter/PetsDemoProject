import json
import logging


class FileUtils:
    @staticmethod
    def read_json(file_address):
        logging.getLogger().info(f"Reading file {file_address}")
        f = open(file_address)
        return json.load(f)
