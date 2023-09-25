import requests
from requests.auth import HTTPBasicAuth


class ApiUtils:
    @staticmethod
    def make_get_request(base_url, endpoint, username, password):
        url = base_url + endpoint
        return requests.get(url, auth=HTTPBasicAuth(username, password))

    @staticmethod
    def make_post_request(base_url, endpoint, username, password, data_as_dict):
        url = base_url + endpoint
        return requests.post(url, json=data_as_dict, auth=HTTPBasicAuth(username, password))

    @staticmethod
    def make_put_request(base_url, endpoint, username, password, data_as_dict, params_as_dict):
        url = base_url + endpoint
        return requests.put(url, json=data_as_dict, params=params_as_dict, auth=HTTPBasicAuth(username, password))

    @staticmethod
    def make_delete_request(base_url, endpoint, username, password, params_as_dict):
        url = base_url + endpoint
        return requests.delete(url, params=params_as_dict, auth=HTTPBasicAuth(username, password))

    @staticmethod
    def make_post_request_wo_creds(base_url, endpoint, params_as_dict):
        url = base_url + endpoint
        return requests.post(url, json=params_as_dict)
