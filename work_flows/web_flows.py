import allure
import time

from extensions.ui_actions import UIActions
import utilities.manage_pages as page


class WebFlows:
    @staticmethod
    @allure.step("Business Flow: Login")
    def login(user: str, password: str):
        UIActions.update_text(page.web_login.get_username_field(), user)
        UIActions.update_text(page.web_login.get_password_field(), password)
        UIActions.click(page.web_login.get_login_btn())
        UIActions.click(page.web_login.get_skip_btn())

    @staticmethod
    @allure.step("Business Flow: Create New User")
    def create_new_user(user: str, email: str, username: str, password: str):
        UIActions.click(page.web_admin_main_page.get_new_user())
        UIActions.update_text(page.web_create_new_user.get_name_field(), user)
        UIActions.update_text(page.web_create_new_user.get_email_field(), email)
        UIActions.update_text(page.web_create_new_user.get_username_field(), username)
        UIActions.update_text(page.web_create_new_user.get_password_field(), password)
        UIActions.click(page.web_create_new_user.get_create_user_button())

    @staticmethod
    @allure.step("Business Flow: Delete Last User")
    def delete_last_user():
        row_list = page.web_admin_main_page.get_rows()
        UIActions.click(row_list[len(row_list) - 1])
        UIActions.click(page.web_new_user_page.get_delete_user_btn())
        UIActions.click(page.web_new_user_page.get_conf_delete_user_btn())
        time.sleep(2)

    @staticmethod
    @allure.step("Business Flow: Login From DB")
    def sign_in_to_conduit_web_with_db_details(email: str, password: str):
        UIActions.click(page.db_web_conduit_menu_head.get_sign_in_field())
        UIActions.update_text(page.db_web_conduit_sign_in.get_email_field(), email)
        UIActions.update_text(page.db_web_conduit_sign_in.get_password_field(), password)
        UIActions.click(page.db_web_conduit_sign_in.get_sign_in_btn())



