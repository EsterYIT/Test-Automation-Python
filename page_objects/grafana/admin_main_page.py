from selenium.webdriver.common.by import By

rows = (By.XPATH, "//tbody/tr")
new_user_btn = (By.CLASS_NAME, "css-1mhnkuh")


class AdminMainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_rows(self):
        return self.driver.find_elements(rows[0], rows[1])

    def get_new_user(self):
        return self.driver.find_element(*new_user_btn)
