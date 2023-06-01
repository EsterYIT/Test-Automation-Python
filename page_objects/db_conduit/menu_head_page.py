from selenium.webdriver.common.by import By

sign_in_field = (By.LINK_TEXT, "Sign in")


class MenuHead:

    def __init__(self, driver):
        self.driver = driver

    def get_sign_in_field(self):
        return self.driver.find_element(*sign_in_field)
