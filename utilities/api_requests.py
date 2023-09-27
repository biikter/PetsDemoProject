from utilities.file_utils import FileUtils
from utilities.api_utils import ApiUtils
from constants import config_data_keys, file_paths, json_keys


class ApiRequests:
    def __init__(self):
        self.config_data = FileUtils.read_json(file_paths.CONFIG_DATA_PATH)
        self.test_data = FileUtils.read_json(file_paths.TEST_DATA_PATH)

        self.base_url = self.config_data[config_data_keys.URL_KEY]
        self.username = self.config_data[config_data_keys.USERNAME_KEY]
        self.password = self.config_data[config_data_keys.PASSWORD_KEY]

    def get_list_of_categories(self):
        endpoint = self.config_data[config_data_keys.ENDPOINT_CATEGORY_KEY]
        return ApiUtils.make_get_request(self.base_url, endpoint, self.username, self.password)

    def create_category(self, animal_name):
        endpoint = self.config_data[config_data_keys.ENDPOINT_CATEGORY_KEY]
        category_data = {json_keys.NAME: animal_name}
        return ApiUtils.make_post_request(self.base_url, endpoint, self.username, self.password, category_data)

    def get_category_by_id(self, category_id):
        endpoint = self.config_data[config_data_keys.ENDPOINT_CATEGORY_BY_ID_KEY].format(category_id)
        return ApiUtils.make_get_request(self.base_url, endpoint, self.username, self.password)

    def update_category(self, category_id, animal_name):
        endpoint = self.config_data[config_data_keys.ENDPOINT_CATEGORY_BY_ID_KEY].format(category_id)
        params = {json_keys.ID: category_id}
        category_data = {json_keys.NAME: animal_name}
        return ApiUtils.make_put_request(self.base_url, endpoint, self.username, self.password, category_data, params)

    def delete_category(self, category_id):
        endpoint = self.config_data[config_data_keys.ENDPOINT_CATEGORY_BY_ID_KEY].format(category_id)
        params = {json_keys.ID: category_id}
        return ApiUtils.make_delete_request(self.base_url, endpoint, self.username, self.password, params)

    def get_list_of_pets(self):
        endpoint = self.config_data[config_data_keys.ENDPOINT_PET_KEY]
        return ApiUtils.make_get_request(self.base_url, endpoint, self.username, self.password)

    def create_pet(self, pet_name, photo_url, category_name, status):
        endpoint = self.config_data[config_data_keys.ENDPOINT_PET_KEY]
        pet_data = {
            json_keys.NAME: pet_name,
            json_keys.PHOTO_URL: photo_url,
            json_keys.CATEGORY: {
                json_keys.NAME: category_name
            },
            json_keys.STATUS: status
        }
        return ApiUtils.make_post_request(self.base_url, endpoint, self.username, self.password, pet_data)

    def get_pet_by_id(self, pet_id):
        endpoint = self.config_data[config_data_keys.ENDPOINT_PET_BY_ID_KEY].format(pet_id)
        return ApiUtils.make_get_request(self.base_url, endpoint, self.username, self.password)

    def update_pet(self, pet_id, pet_name, photo_url, category_name, status):
        endpoint = self.config_data[config_data_keys.ENDPOINT_PET_BY_ID_KEY].format(pet_id)
        params = {json_keys.ID: pet_id}
        pet_data = {
            json_keys.NAME: pet_name,
            json_keys.PHOTO_URL: photo_url,
            json_keys.CATEGORY: {
                json_keys.NAME: category_name
            },
            json_keys.STATUS: status
        }
        return ApiUtils.make_put_request(self.base_url, endpoint, self.username, self.password, pet_data, params)

    def delete_pet(self, pet_id):
        endpoint = self.config_data[config_data_keys.ENDPOINT_PET_BY_ID_KEY].format(pet_id)
        params = {json_keys.ID: pet_id}
        return ApiUtils.make_delete_request(self.base_url, endpoint, self.username, self.password, params)

    def get_token(self):
        endpoint = self.config_data[config_data_keys.ENDPOINT_TOKEN_KEY]
        request_body = {
            json_keys.USERNAME: self.config_data[config_data_keys.USERNAME_KEY],
            json_keys.PASSWORD: self.config_data[config_data_keys.PASSWORD_KEY]
        }
        return ApiUtils.make_post_request_wo_creds(self.base_url, endpoint, request_body)
