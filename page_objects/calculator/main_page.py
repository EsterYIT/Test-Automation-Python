from selenium.webdriver.common.by import By

one_btn = (By.XPATH, "//*[@AutomationId='num1Button']")
plus_btn = (By.XPATH, "//*[@AutomationId='plusButton']")
eight_btn = (By.XPATH, "//*[@AutomationId='num8Button']")
equal_btn = (By.XPATH, "//*[@AutomationId='equalButton']")
clear_btn = (By.XPATH, "//*[@AutomationId='clearButton']")
result_field = (By.XPATH, "//*[@AutomationId='CalculatorResults']")


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_one_btn(self):
        return self.driver.find_element(*one_btn)

    def get_plus_btn(self):
        return self.driver.find_element(*plus_btn)

    def get_eight_btn(self):
        return self.driver.find_element(*eight_btn)

    def get_equal_btn(self):
        return self.driver.find_element(*equal_btn)

    def get_clear_btn(self):
        return self.driver.find_element(*clear_btn)

    def get_result_field(self):
        return self.driver.find_element(*result_field)
