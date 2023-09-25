import json


class FileUtils():
    @staticmethod
    def read_json(file_address):
        f = open(file_address)
        return json.load(f)
