from selenium.webdriver.common.by import By

amount_field = (By.ID, "etAmount")
term_field = (By.ID, "etTerm")
rate_field = (By.ID, "etRate")
calc_btn = (By.ID, "btnCalculate")
repayment_txt = (By.ID, "tvRepayment")


class MainPageMortgage:

    def __init__(self, driver):
        self.driver = driver

    def get_amount_field(self):
        return self.driver.find_element(*amount_field)

    def get_term_field(self):
        return self.driver.find_element(*term_field)

    def get_rate_field(self):
        return self.driver.find_element(*rate_field)

    def get_calc_btn(self):
        return self.driver.find_element(*calc_btn)

    def get_repayment_txt(self):
        return self.driver.find_element(*repayment_txt)
