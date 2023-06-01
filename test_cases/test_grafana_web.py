import pytest
import allure
from extensions.ui_actions import UIActions
from work_flows.web_flows import WebFlows
from utilities.common_ops import get_data
from extensions.verifications import Verifications
import utilities.manage_pages as page


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:

    @allure.title("Test01 - Verify Header")
    @allure.description("This test login and verifies the main header")
    def test01_verify_header(self):
        WebFlows.login(get_data("username"), get_data("password"))
        print("actual = ", page.web_main.get_header_txt().text)
        Verifications.verify_text_element(page.web_main.get_header_txt(), "Welcome to Grafana")

    @allure.title("Test02 - Verify Default User")
    @allure.description("This test verifies the default user")
    def test02_verify_default_users(self):
        UIActions.mouse_hover(page.web_left_menu.get_server_btn(), page.web_admin_menu_page.get_users_link())
        Verifications.number_of_elements(page.web_admin_main_page.get_rows(), 1)

    @allure.title("Test03 - Verify New User")
    @allure.description("This test verifies a new user has been added")
    def test03_verify_new_user(self):
        UIActions.mouse_hover(page.web_left_menu.get_server_btn(), page.web_admin_menu_page.get_users_link())
        WebFlows.create_new_user("bbb", "bb@gmail.com", "ester", "654321")
        Verifications.verify_text_element(page.web_new_user_page.get_new_user_page(), "User informatio")

    @allure.title("Test04 - Verify User Deletion")
    @allure.description("This test verifies a user has been deleted")
    def test04_verify_user_deletion(self):
        WebFlows.delete_last_user()
        Verifications.number_of_elements(page.web_admin_main_page.get_rows(), 1)

