import requests
from utilities.json_utils import JsonUtils
from utilities.file_utils import FileUtils
from utilities.api_requests import ApiRequests
from constants import file_paths, json_keys, test_data_keys

test_data = FileUtils.read_json(file_paths.TEST_DATA_PATH)
api_requests = ApiRequests()


def test_get_list_of_categories():
    response = api_requests.get_list_of_categories()
    assert response.status_code == requests.codes.ok

    category_list_schema = FileUtils.read_json(file_paths.CATEGORY_LIST_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_list_schema)


def test_create_category():
    response = api_requests.create_category(test_data[test_data_keys.ANIMAL_NAME_KEY])
    assert response.status_code == requests.codes.created

    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_schema)

    print(response.json()[json_keys.ID])
    test_data.update({test_data_keys.NEW_CATEGORY_ID_KEY: response.json()[json_keys.ID]})


def test_create_existing_category():
    response = api_requests.create_category(test_data[test_data_keys.EXISTING_CATEGORY_NAME_KEY])
    assert response.status_code == requests.codes.internal_server_error


def test_get_category_by_id():
    response = api_requests.get_category_by_id(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.ok

    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_schema)
    assert response.json()[json_keys.NAME] == test_data[test_data_keys.ANIMAL_NAME_KEY]


def test_get_category_by_false_id():
    response = api_requests.get_category_by_id(test_data[test_data_keys.FALSE_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.not_found


def test_update_category():
    response = api_requests.update_category(test_data[test_data_keys.NEW_CATEGORY_ID_KEY], test_data[
        test_data_keys.ANIMAL_NAME_2_KEY])
    assert response.status_code == requests.codes.ok

    category_schema = FileUtils.read_json(file_paths.CATEGORY_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), category_schema)

    assert response.json()[json_keys.NAME] == test_data[test_data_keys.ANIMAL_NAME_2_KEY]


def test_update_category_false_id():
    response = api_requests.update_category(test_data[test_data_keys.FALSE_CATEGORY_ID_KEY], test_data[
        test_data_keys.ANIMAL_NAME_2_KEY])
    assert response.status_code == requests.codes.not_found


def test_update_category_existing_name():
    response = api_requests.update_category(test_data[test_data_keys.NEW_CATEGORY_ID_KEY], test_data[
        test_data_keys.EXISTING_CATEGORY_NAME_KEY])
    assert response.status_code == requests.codes.internal_server_error


def test_delete_category():
    response = api_requests.delete_category(test_data[test_data_keys.NEW_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.no_content
    assert response.text == ""


def test_delete_category_false_id():
    response = api_requests.delete_category(test_data[test_data_keys.FALSE_CATEGORY_ID_KEY])
    assert response.status_code == requests.codes.not_found


def test_get_list_of_pets():
    response = api_requests.get_list_of_pets()
    assert response.status_code == requests.codes.ok

    pet_list_schema = FileUtils.read_json(file_paths.PET_LIST_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_list_schema)


def test_create_pet():
    response = api_requests.create_pet(
        test_data[test_data_keys.PET_NAME_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_KEY],
        test_data[test_data_keys.PET_STATUS_KEY]
    )
    assert response.status_code == requests.codes.created

    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_schema)
    
    print(response.json()[json_keys.ID])
    test_data.update({test_data_keys.NEW_PET_ID_KEY: response.json()[json_keys.ID]})


def test_create_pet_with_existing_name():
    response = api_requests.create_pet(
        test_data[test_data_keys.EXISTING_PET_NAME_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_KEY],
        test_data[test_data_keys.PET_STATUS_KEY]
    )
    assert response.status_code == requests.codes.internal_server_error


def test_create_pet_with_false_category():
    response = api_requests.create_pet(
        test_data[test_data_keys.PET_NAME_3_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_KEY],
        test_data[test_data_keys.FALSE_CATEGORY_NAME_KEY],
        test_data[test_data_keys.PET_STATUS_KEY]
    )
    assert response.status_code == requests.codes.not_found


def test_get_pet_by_id():
    response = api_requests.get_pet_by_id(test_data[test_data_keys.NEW_PET_ID_KEY])
    assert response.status_code == requests.codes.ok

    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_schema)

    assert response.json()[json_keys.NAME] == test_data[test_data_keys.PET_NAME_KEY]
    assert response.json()[json_keys.PHOTO_URL] == test_data[test_data_keys.PET_PHOTO_URL_KEY]
    assert response.json()[json_keys.CATEGORY][json_keys.NAME] == test_data[test_data_keys.PET_CATEGORY_NAME_KEY]
    assert response.json()[json_keys.STATUS] == test_data[test_data_keys.PET_STATUS_KEY]


def test_get_pet_by_false_id():
    response = api_requests.get_pet_by_id(test_data[test_data_keys.FALSE_PET_ID_KEY])
    assert response.status_code == requests.codes.not_found


def test_update_pet():
    response = api_requests.update_pet(
        test_data[test_data_keys.NEW_PET_ID_KEY],
        test_data[test_data_keys.PET_NAME_2_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_2_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY],
        test_data[test_data_keys.PET_STATUS_2_KEY]
    )
    assert response.status_code == requests.codes.ok

    pet_schema = FileUtils.read_json(file_paths.PET_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), pet_schema)

    assert response.json()[json_keys.NAME] == test_data[test_data_keys.PET_NAME_2_KEY]
    assert response.json()[json_keys.PHOTO_URL] == test_data[test_data_keys.PET_PHOTO_URL_2_KEY]
    assert response.json()[json_keys.CATEGORY][json_keys.NAME] == test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY]
    assert response.json()[json_keys.STATUS] == test_data[test_data_keys.PET_STATUS_2_KEY]


def test_update_pet_with_existing_name():
    response = api_requests.update_pet(
        test_data[test_data_keys.NEW_PET_ID_KEY],
        test_data[test_data_keys.EXISTING_PET_NAME_KEY],
        test_data[test_data_keys.PET_PHOTO_URL_2_KEY],
        test_data[test_data_keys.PET_CATEGORY_NAME_2_KEY],
        test_data[test_data_keys.PET_STATUS_2_KEY]
    )
    assert response.status_code == requests.codes.internal_server_error


def test_delete_pet():
    response = api_requests.delete_pet(test_data[test_data_keys.NEW_PET_ID_KEY])
    assert response.status_code == requests.codes.no_content
    assert response.text == ""


def test_delete_pet_by_false_id():
    response = api_requests.delete_pet(test_data[test_data_keys.FALSE_PET_ID_KEY])
    assert response.status_code == requests.codes.not_found


def test_get_token():
    response = api_requests.get_token()
    assert response.status_code == requests.codes.ok

    token_schema = FileUtils.read_json(file_paths.TOKEN_SCHEMA_PATH)
    assert JsonUtils.validate_json(response.json(), token_schema)
    print(response.json()[json_keys.TOKEN])
