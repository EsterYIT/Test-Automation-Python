import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data('url_api')


class ApiFlows:
    @staticmethod
    @allure.step('Create new user')
    def create_user(id, name, username, email):
        payload = {
                    "id": id,
                    "name": name,
                    "username": username,
                    "email": email,

        }
        status_code = APIActions.post(url + '/users', payload)
        return status_code

    @staticmethod
    @allure.step('Update user details')
    def update_user(email, name, username, id):
        payload = {
                    "id": id,
                    "name": name,
                    "username": username,
                    "email": email,
        }
        status_code = APIActions.put(url + '/users/' + str(id), payload)
        return status_code

    @staticmethod
    @allure.step('Delete user')
    def delete_user(id):
        status_code = APIActions.delete(url + '/users/' + str(id))
        return status_code


