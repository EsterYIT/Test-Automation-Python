from selenium.webdriver.common.by import By

open_drawer_btn = (By.CLASS_NAME, "toggleVisibilityPanel_hNPyc")
status_drawer_btn = (By.XPATH, "//div[@class='statusWrapper_fkjww']/button")


class ToDoDrawer:

    def __init__(self, driver):
        self.driver = driver

    def get_open_drawer_btn(self):
        return self.driver.find_element(*open_drawer_btn)

    def get_status_drawer_btn(self):
        return self.driver.find_elements(*status_drawer_btn)

