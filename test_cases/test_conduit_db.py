import pytest
import allure
from work_flows.db_flows import DBFlows
from extensions.verifications import Verifications
import utilities.manage_pages as page


@pytest.mark.usefixtures('init_db_connection')
class TestConduit:
    @allure.title("Test01 - Login to conduit with DB credentials")
    @allure.description("This test login with DB credentials and verifies user name")
    def test01_login_with_db_credentials(self):
        DBFlows.login_conduit_via_db()
        Verifications.verify_text_element(page.db_web_conduit_user_head.get_user_name(), "moshe")




