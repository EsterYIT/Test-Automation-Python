from selenium.webdriver.common.by import By

user_head_list = (By.XPATH, "//ul[@class='nav navbar-nav pull-xs-right']/li")
user_your_feed_nav = (By.LINK_TEXT, "Your Feed")


class UserHead:

    def __init__(self, driver):
        self.driver = driver

    def get_user_head_list(self):
        return self.driver.find_elements(*user_head_list)

    def get_user_your_feed_nav(self):
        return self.driver.find_element(*user_your_feed_nav)