from selenium.webdriver.common.by import By

users_link = (By.XPATH, "//a[@href='/admin/users']")


class AdminMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_users_link(self):
        return self.driver.find_element(*users_link)
