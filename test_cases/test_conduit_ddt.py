import pytest
import unittest
import allure
from work_flows.web_flows import WebFlows
from ddt import ddt, data, unpack, file_data
import utilities.manage_pages as page
import utilities.common_ops as common
from utilities.common_ops import get_data
from extensions.verifications import Verifications


@pytest.mark.usefixtures('init_web_driver')
@ddt
class TestWebDDT(unittest.TestCase):

    @allure.title("Test01 - Verify Sign In")
    @allure.description("Verifies the sign in header with DDT")
    @data(*common.read_data_from_csv(get_data('DDT_file')))
    @unpack
    def test01_verify_sign_in_header(self, email, password):
        WebFlows.sign_in_to_conduit_web_with_db_details(email, password)
        Verifications.verify_text_element(page.db_web_conduit_user_head.get_user_your_feed_nav(), "Your Feed")

    # To use DDT must get the default scope fixture.
    # Must add to tha class unittest.TestCase/softest.TestCase

