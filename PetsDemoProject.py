import requests
import logging
from utilities.json_utils import JsonUtils
from utilities.file_utils import FileUtils
from utilities.api_requests import ApiRequests
from constants import file_paths, json_keys, test_data_keys

test_data = FileUtils.read_json(file_paths.TEST_DATA_PATH)
api_requests = ApiRequests()
logger = logging.getLogger()


def test_get_list_of_categories():
    response = api_requests.get_list_of_categories()
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    category_list_schema = FileUtils.read_json(file_paths.CATEGORY_LIST_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_list_schema), "JSON schema not valid"


def test_create_category():
    response = api_requests.create_category(test_data[test_data_keys.ANIMAL_NAME_KEY])
    assert response.status_code == requests.codes.created, "Status code is not expected"

    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_schema), "JSON schema not valid"

    logging.getLogger().info("New category id =" + str(response.json()[json_keys.ID]))
    test_data.update({test_data_keys.NEW_CATEGORY_ID_KEY: response.json()[json_keys.ID]})


def test_create_existing_category():
    response = api_requests.create_category(test_data[test_data_keys.EXISTING_CATEGORY_NAME_KEY])
    assert response.status_code == requests.codes.internal_server_error, "Status code is not expected"


def test_get_category_by_id():
    response = api_requests.get_category_by_id(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_schema), "JSON schema not valid"
    assert response.json()[json_keys.NAME] == test_data[test_data_keys.ANIMAL_NAME_KEY], "Category name is not expected"


def test_get_category_by_false_id():
    response = api_requests.get_category_by_id(test_data[test_data_keys.FALSE_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.not_found, "Status code is not expected"


def test_update_category():
    response = api_requests.update_category(test_data[test_data_keys.NEW_CATEGORY_ID_KEY], test_data[
        test_data_keys.ANIMAL_NAME_2_KEY])
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_schema), "JSON schema not valid"

    assert response.json()[json_keys.NAME] == test_data[test_data_keys.ANIMAL_NAME_2_KEY], "Category name is not expected"


def test_update_category_false_id():
    response = api_requests.update_category(test_data[test_data_keys.FALSE_CATEGORY_ID_KEY], test_data[
        test_data_keys.ANIMAL_NAME_2_KEY])
    assert response.status_code == requests.codes.not_found, "Status code is not expected"


def test_update_category_existing_name():
    response = api_requests.update_category(test_data[test_data_keys.NEW_CATEGORY_ID_KEY], test_data[
        test_data_keys.EXISTING_CATEGORY_NAME_KEY])
    assert response.status_code == requests.codes.internal_server_error, "Status code is not expected"


def test_delete_category():
    response = api_requests.delete_category(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.no_content, "Status code is not expected"
    assert response.text == "", "Response body is not empty"


def test_delete_category_false_id():
    response = api_requests.delete_category(test_data[test_data_keys.FALSE_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.not_found, "Status code is not expected"


def test_get_list_of_pets():
    response = api_requests.get_list_of_pets()
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    pet_list_schema = FileUtils.read_json(file_paths.PET_LIST_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_list_schema), "JSON schema not valid"


def test_create_pet():
    response = api_requests.create_pet(
        test_data[test_data_keys.PET_NAME_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_KEY],
        test_data[test_data_keys.PET_STATUS_KEY]
    )
    assert response.status_code == requests.codes.created, "Status code is not expected"

    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_schema), "JSON schema not valid"
    
    logging.getLogger().info("New pet id =" + str(response.json()[json_keys.ID]))
    test_data.update({test_data_keys.NEW_PET_ID_KEY: response.json()[json_keys.ID]})


def test_create_pet_with_existing_name():
    response = api_requests.create_pet(
        test_data[test_data_keys.EXISTING_PET_NAME_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_KEY],
        test_data[test_data_keys.PET_STATUS_KEY]
    )
    assert response.status_code == requests.codes.internal_server_error, "Status code is not expected"


def test_create_pet_with_false_category():
    response = api_requests.create_pet(
        test_data[test_data_keys.PET_NAME_3_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_KEY],
        test_data[test_data_keys.FALSE_CATEGORY_NAME_KEY],
        test_data[test_data_keys.PET_STATUS_KEY]
    )
    assert response.status_code == requests.codes.not_found, "Status code is not expected"


def test_get_pet_by_id():
    response = api_requests.get_pet_by_id(test_data[test_data_keys.NEW_PET_ID_KEY])
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_schema), "JSON schema not valid"

    assert response.json()[json_keys.NAME] == test_data[test_data_keys.PET_NAME_KEY], "Pet name is not expected"
    assert response.json()[json_keys.PHOTO_URL] == test_data[test_data_keys.PET_PHOTO_URL_KEY], "Pet photo_url is not expected"
    assert response.json()[json_keys.CATEGORY][json_keys.NAME] == test_data[test_data_keys.PET_CATEGORY_NAME_KEY], "Pet category is not expected"
    assert response.json()[json_keys.STATUS] == test_data[test_data_keys.PET_STATUS_KEY], "Pet status is not expected"


def test_get_pet_by_false_id():
    response = api_requests.get_pet_by_id(test_data[test_data_keys.FALSE_PET_ID_KEY])
    assert response.status_code == requests.codes.not_found, "Status code is not expected"


def test_update_pet():
    response = api_requests.update_pet(
        test_data[test_data_keys.NEW_PET_ID_KEY],
        test_data[test_data_keys.PET_NAME_2_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_2_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY],
        test_data[test_data_keys.PET_STATUS_2_KEY]
    )
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_schema), "JSON schema not valid"

    assert response.json()[json_keys.NAME] == test_data[test_data_keys.PET_NAME_2_KEY], "Pet name is not expected"
    assert response.json()[json_keys.PHOTO_URL] == test_data[test_data_keys.PET_PHOTO_URL_2_KEY], "Pet photo_url is not expected"
    assert response.json()[json_keys.CATEGORY][json_keys.NAME] == test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY], "Pet category is not expected"
    assert response.json()[json_keys.STATUS] == test_data[test_data_keys.PET_STATUS_2_KEY], "Pet status is not expected"


def test_update_pet_with_existing_name():
    response = api_requests.update_pet(
        test_data[test_data_keys.NEW_PET_ID_KEY],
        test_data[test_data_keys.EXISTING_PET_NAME_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_2_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY],
        test_data[test_data_keys.PET_STATUS_2_KEY]
    )
    assert response.status_code == requests.codes.internal_server_error, "Status code is not expected"


def test_delete_pet():
    response = api_requests.delete_pet(test_data[test_data_keys.NEW_PET_ID_KEY])
    assert response.status_code == requests.codes.no_content, "Status code is not expected"
    assert response.text == "", "Response body is not empty"


def test_delete_pet_by_false_id():
    response = api_requests.delete_pet(test_data[test_data_keys.FALSE_PET_ID_KEY])
    assert response.status_code == requests.codes.not_found, "Status code is not expected"


def test_get_token():
    response = api_requests.get_token()
    assert response.status_code == requests.codes.ok, "Status code is not expected"

    token_schema = FileUtils.read_json(file_paths.TOKEN_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), token_schema), "JSON schema not valid"
    print(response.json()[json_keys.TOKEN])
