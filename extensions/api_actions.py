import allure
import requests

header = {'content-type': 'application/json'}


class APIActions:
    @staticmethod
    @allure.step('GET All Users Data')
    def get_api_url(path):
        response = requests.get(path)
        return response

    @staticmethod
    @allure.step('POST - Create New User')
    def post(path, payload):
        response = requests.post(path,  json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step('PUT - Update User Data')
    def put(path, payload):
        response = requests.put(path,  json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step('Delete User')
    def delete(path):
        response = requests.delete(path)
        return response.status_code