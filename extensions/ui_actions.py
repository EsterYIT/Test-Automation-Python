
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf
import utilities.common_ops as common


class UIActions:
    @staticmethod
    @allure.step('click on element')
    def click(elem: WebElement):
        common.wait_until_element_is_clickable(elem)
        elem.click()

    @staticmethod
    @allure.step('updating text')
    def update_text(elem: WebElement, value: str):
        common.wait_until_element_is_visible(elem)
        elem.send_keys(value)

    @staticmethod
    @allure.step('mouse hover on one element')
    def mouse_hover(elem: WebElement):
        conf.action.move_to_element(elem).perform()

    @staticmethod
    @allure.step('mouse hover on two elements')
    def mouse_hover2(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Press Keyboard key')
    def press_key(elem: WebElement, key: Keys):
        elem.send_keys(key)

    @staticmethod
    @allure.step('right click on element')
    def right_click(elem: WebElement):
        common.wait_until_element_is_clickable(elem)
        conf.action.context_click(elem).perform()

    @staticmethod
    @allure.step('drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step('clear text field in element')
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step('go back to last page')
    def back():
        conf.driver.back()

    @staticmethod
    @allure.step('go back twice(in page)')
    def double_back():
        conf.driver.back()
        conf.driver.back()
