from selenium.webdriver.common.by import By

username_field = (By.NAME, "user")
password_field = (By.ID, "current-password")
login_btn = (By.CSS_SELECTOR, "button[type='submit']")
skip_btn = (By.CLASS_NAME, "css-1kf0ycc-button")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(*username_field)

    def get_password_field(self):
        return self.driver.find_element(*password_field)

    def get_login_btn(self):
        return self.driver.find_element(*login_btn)

    def get_skip_btn(self):
        return self.driver.find_element(*skip_btn)

