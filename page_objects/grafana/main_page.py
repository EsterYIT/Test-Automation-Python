from selenium.webdriver.common.by import By

header_txt = (By.CLASS_NAME, "css-17tm80")


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_header_txt(self):
        return self.driver.find_element(*header_txt)
