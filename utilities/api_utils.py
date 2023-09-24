import requests
from requests.auth import HTTPBasicAuth

class Api_Utils():
    @staticmethod
    def make_get_request(base_url, endpoint, username, password):
        url = base_url + endpoint
        return requests.get(url, auth=HTTPBasicAuth(username, password))
