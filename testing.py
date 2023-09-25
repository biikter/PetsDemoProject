import requests
from utilities.api_utils import ApiUtils
from utilities.json_utils import JsonUtils
from utilities.file_utils import FileUtils
import file_paths
import config_data_keys
import test_data_keys

config_data = FileUtils.read_json(file_paths.CONFIG_DATA_PATH)
test_data = FileUtils.read_json(file_paths.TEST_DATA_PATH)

base_url = config_data[config_data_keys.URL_KEY]
username = config_data[config_data_keys.USERNAME_KEY]
password = config_data[config_data_keys.PASSWORD_KEY]


def test_get_list_of_categories():
    category_list_schema = FileUtils.read_json(file_paths.CATEGORY_LIST_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_CATEGORY_KEY]
    response = ApiUtils.make_get_request(base_url, endpoint, username, password)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), category_list_schema)


def test_create_category():
    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_CATEGORY_KEY]
    category_data = {test_data[test_data_keys.CATEGORY_KEY]: test_data[test_data_keys.ANIMAL_NAME_KEY]}
    response = ApiUtils.make_post_request(base_url, endpoint, username, password, category_data)

    assert response.status_code == requests.codes.created
    assert JsonUtils.validate_json(response.json(), category_schema)

    print(response.json()['id'])
    test_data.update({test_data_keys.NEW_CATEGORY_ID_KEY: response.json()['id']})


def test_get_category_by_id():
    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_CATEGORY_BY_ID_KEY].format(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    response = ApiUtils.make_get_request(base_url, endpoint, username, password)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), category_schema)
    assert response.json()['name'] == test_data[test_data_keys.ANIMAL_NAME_KEY]


def test_update_category():
    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_CATEGORY_BY_ID_KEY].format(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    params = {'id': test_data[test_data_keys.NEW_CATEGORY_ID_KEY]}
    category_data = {'name': test_data[test_data_keys.ANIMAL_NAME_2_KEY]}
    response = ApiUtils.make_put_request(base_url, endpoint, username, password, category_data, params)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), category_schema)
    assert response.json()['name'] == test_data[test_data_keys.ANIMAL_NAME_2_KEY]


def test_delete_category():
    endpoint = config_data[config_data_keys.ENDPOINT_CATEGORY_BY_ID_KEY].format(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    params = {'id': test_data[test_data_keys.NEW_CATEGORY_ID_KEY]}
    response = ApiUtils.make_delete_request(base_url, endpoint, username, password, params)

    assert response.status_code == requests.codes.no_content
    assert response.text == ""


def test_get_list_of_pets():
    pet_list_schema = FileUtils.read_json(file_paths.PET_LIST_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_PET_KEY]
    response = ApiUtils.make_get_request(base_url, endpoint, username, password)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), pet_list_schema)


def test_create_pet():
    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_PET_KEY]
    pet_data = {'name': test_data[test_data_keys.PET_NAME_KEY],
                'photo_url': test_data[test_data_keys.PET_PHOTO_URL_KEY],
                'category': {
                    'name': test_data[test_data_keys.PET_CATEGORY_NAME_KEY]
                    },
                'status': test_data[test_data_keys.PET_STATUS_KEY]
                }
    response = ApiUtils.make_post_request(base_url, endpoint, username, password, pet_data)

    assert response.status_code == requests.codes.created
    assert JsonUtils.validate_json(response.json(), pet_schema)
    print(response.json()['id'])
    test_data.update({test_data_keys.NEW_PET_ID_KEY: response.json()['id']})


def test_get_pet_by_id():
    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_PET_BY_ID_KEY].format(test_data[test_data_keys.NEW_PET_ID_KEY])
    response = ApiUtils.make_get_request(base_url, endpoint, username, password)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), pet_schema)
    assert response.json()['name'] == test_data[test_data_keys.PET_NAME_KEY]
    assert response.json()['photo_url'] == test_data[test_data_keys.PET_PHOTO_URL_KEY]
    assert response.json()['category']['name']== test_data[test_data_keys.PET_CATEGORY_NAME_KEY]
    assert response.json()['status'] == test_data[test_data_keys.PET_STATUS_KEY]


def test_update_pet_by_id():
    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_PET_BY_ID_KEY].format(test_data[test_data_keys.NEW_PET_ID_KEY])
    params = {'id': test_data[test_data_keys.NEW_PET_ID_KEY]}
    pet_data = {'name': test_data[test_data_keys.PET_NAME_2_KEY],
                'photo_url': test_data[test_data_keys.PET_PHOTO_URL_2_KEY],
                'category': {
                    'name': test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY]
                    },
                'status': test_data[test_data_keys.PET_STATUS_2_KEY]
                }
    response = ApiUtils.make_put_request(base_url, endpoint, username, password, pet_data, params)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), pet_schema)
    assert response.json()['name'] == test_data[test_data_keys.PET_NAME_2_KEY]
    assert response.json()['photo_url'] == test_data[test_data_keys.PET_PHOTO_URL_2_KEY]
    assert response.json()['category']['name']== test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY]
    assert response.json()['status'] == test_data[test_data_keys.PET_STATUS_2_KEY]


def test_delete_pet():
    endpoint = config_data[config_data_keys.ENDPOINT_PET_BY_ID_KEY].format(test_data[test_data_keys.NEW_PET_ID_KEY])
    params = {'id': test_data[test_data_keys.NEW_PET_ID_KEY]}
    response = ApiUtils.make_delete_request(base_url, endpoint, username, password, params)

    assert response.status_code == requests.codes.no_content
    assert response.text == ""


def test_get_token():
    token_schema = FileUtils.read_json(file_paths.TOKEN_SCHEMA_PATH)
    endpoint = config_data[config_data_keys.ENDPOINT_TOKEN_KEY]
    request_body = {
        'username': config_data[config_data_keys.USERNAME_KEY],
        'password': config_data[config_data_keys.PASSWORD_KEY]
        }
    response = ApiUtils.make_post_request_wo_creds(base_url, endpoint, request_body)

    assert response.status_code == requests.codes.ok
    assert JsonUtils.validate_json(response.json(), token_schema)
    print(response.json()['token'])
