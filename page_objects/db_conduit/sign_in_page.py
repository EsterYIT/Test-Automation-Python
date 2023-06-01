from selenium.webdriver.common.by import By

email_field = (By.XPATH, "//input[@type='email']")
password_field = (By.XPATH, "//input[@type='password']")
sign_in_btn = (By.XPATH, "//button[@type='submit']")


class SignInPage:

    def __init__(self, driver):
        self.driver = driver

    def get_email_field(self):
        return self.driver.find_element(*email_field)

    def get_password_field(self):
        return self.driver.find_element(*password_field)

    def get_sign_in_btn(self):
        return self.driver.find_element(*sign_in_btn)