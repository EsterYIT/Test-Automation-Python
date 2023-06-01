import allure
from extensions.verifications import Verifications
from work_flows.api_flows import ApiFlows


id = 11
name = 'ester'
username = 'es'
email = 'es@gmail.com'


class TestApi:

    @allure.title('Test 01 : Create User And Verify Status Code')
    @allure.description('this test create a new user')
    def test_create_and_verify_user(self):
        actual = ApiFlows.create_user(id, name, username, email)
        Verifications.number_in_number(actual, 201)

    @allure.title('Test 02 : Update User And Verify Status Code')
    @allure.description('this test update user and verify status code"')
    def test_update_and_verify_user_name(self):

        actual = ApiFlows.update_user(email, name + ' yitzhak', username, id)
        Verifications.number_in_number(actual, 200)

    @allure.title('Test 03 : Delete User And Verify Status Code')
    @allure.description('this test delete user and verify status code"')
    def test_delete_user(self):
        actual = ApiFlows.delete_user(11)
        Verifications.number_in_number(actual, 200)

    # #Pretty print
    # data = APIActions.get_api_url(get_data('url_api') + '/users')
    # pretty_json = json.loads(data.text)
    # print(json.dumps(pretty_json, indent=2))