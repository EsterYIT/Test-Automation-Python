from selenium.webdriver.common.by import By

new_user_page = (By.XPATH, "//div[@class='page-container page-body']/h3[1]")
delete_user_btn = (By.XPATH, "//div[@class='css-wxwti7']//button[1]")
conf_delete_user_btn = (By.XPATH, "//button[@aria-label='Confirm Modal Danger Button']")


class NewUserMainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_new_user_page(self):
        return self.driver.find_element(*new_user_page)

    def get_delete_user_btn(self):
        return self.driver.find_element(*delete_user_btn)

    def get_conf_delete_user_btn(self):
        return self.driver.find_element(*conf_delete_user_btn)