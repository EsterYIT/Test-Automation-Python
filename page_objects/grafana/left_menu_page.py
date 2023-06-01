from selenium.webdriver.common.by import By

server_btn = (By.XPATH, "//ul[@class='css-kmtjxr']//li[7]")


class LeftMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_server_btn(self):
        return self.driver.find_element(server_btn[0], server_btn[1])
