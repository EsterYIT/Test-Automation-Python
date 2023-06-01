import allure
import utilities.manage_pages as page


class DesktopFlows:

    @staticmethod
    @allure.step("Business Flow: Calculate Addition: 1 + 8")
    def calculate_addition():
        page.desktop_main.get_clear_btn().click()
        page.desktop_main.get_one_btn().click()
        page.desktop_main.get_plus_btn().click()
        page.desktop_main.get_eight_btn().click()
        page.desktop_main.get_equal_btn().click()

