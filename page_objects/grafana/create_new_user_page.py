from selenium.webdriver.common.by import By

name_field = (By.ID, "name-input")
email_field = (By.ID, "email-input")
username_field = (By.ID, "username-input")
password_field = (By.ID, "password-input")
create_user_button = (By.CLASS_NAME, "css-1sara2j-button")


class CreateNewUser:

    def __init__(self, driver):
        self.driver = driver

    def get_name_field(self):
        return self.driver.find_element(*name_field)

    def get_email_field(self):
        return self.driver.find_element(*email_field)

    def get_username_field(self):
        return self.driver.find_element(*username_field)

    def get_password_field(self):
        return self.driver.find_element(*password_field)

    def get_create_user_button(self):
        return self.driver.find_element(*create_user_button)
