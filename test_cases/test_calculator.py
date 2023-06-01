import pytest
import allure
from work_flows.desktop_flows import DesktopFlows
from extensions.verifications import Verifications
import utilities.manage_pages as page


@pytest.mark.usefixtures('init_desktop_driver')
class TestDesktop:

    @allure.title("Test01 - Verify Addition Command")
    @allure.description("This test verifies the addition command")
    def test01_verify_addition_command(self):
        DesktopFlows.calculate_addition()
        Verifications.verify_text_element(page.desktop_main.get_result_field(), "התצוגה היא 9")
