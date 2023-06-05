import allure
from selenium.webdriver.remote.webelement import WebElement
import utilities.common_ops as common


class Verifications:

    @staticmethod
    @allure.step("Verify Text In Element")
    def verify_text_element(elem: WebElement, expected: str):
        common.wait_until_element_is_visible(elem)
        print("99999999999 ", elem.text)
        assert elem.text == expected

    @staticmethod
    @allure.step("Verify Number Of Element")
    def number_of_elements(elements: list, expected: int):
        assert len(elements) == expected

    @staticmethod
    @allure.step("Verify Visibility Of Element")
    def visible_of_element(element: WebElement):
        assert element.is_displayed()

    @staticmethod
    @allure.step("Verify Number In Number")
    def number_in_number(actual: int, expected: int):
        assert actual == expected



