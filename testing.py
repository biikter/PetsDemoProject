import json
from utilities.api_utils import Api_Utils
from utilities.json_utils import Json_Utils

def test_schema():
    sc = open('schemas/pet_schema.json')
    pet_schema = json.load(sc)

    f = open('data/config_data.json')
    config_data = json.load(f)
    #api_url = config_data['url'] + config_data['endpoint_pet_by_id']
    #response = requests.get(api_url, auth=HTTPBasicAuth(username, password))
    username = config_data['username']
    password = config_data['password']
    base_url = config_data['url']
    endpoint = config_data['endpoint_pet_by_id']
    response = Api_Utils.make_get_request(base_url, endpoint, username, password)

    print(response.json())

    assert Json_Utils.validateJson(response.json(), pet_schema)

def test_dummy():
    assert True