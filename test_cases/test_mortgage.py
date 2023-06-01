import allure
import pytest
from extensions.verifications import Verifications
from work_flows.mobile_flows import MobileFlows
import utilities.manage_pages as page


@pytest.mark.usefixtures('init_mobile_driver')
class TestMobile:
    @allure.title('Test01: Verify Mortgage Repayment')
    @allure.description('this test verifies the mortgage repayment')
    def test_verify_repayment(self):
        MobileFlows.calculate_mortgage('1000', '3', '4')
        Verifications.verify_text_element(page.mobile_mortgage_main.get_repayment_txt(), "£30.03")