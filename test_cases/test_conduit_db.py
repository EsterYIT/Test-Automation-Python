import pytest
import allure
from work_flows.db_flows import DBFlows
from extensions.verifications import Verifications
import utilities.manage_pages as page
import time


@pytest.mark.usefixtures('init_db_connection')
class TestConduit:
    @allure.title("Test01 - Login to conduit with DB credentials")
    @allure.description("This test login with DB credentials and verifies user name")
    def test01_login_with_db_credentials(self):
        DBFlows.login_conduit_via_db()
        time.sleep(2)
        size = len(page.db_web_conduit_user_head.get_user_head_list())
        username = page.db_web_conduit_user_head.get_user_head_list()[size-1]
        Verifications.verify_text_element(username, "moshe")




