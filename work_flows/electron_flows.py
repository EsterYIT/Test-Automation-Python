
import allure
from extensions.ui_actions import UIActions
from selenium.webdriver.common.keys import Keys
import utilities.manage_pages as page


class ElectronFlows:

    @staticmethod
    @allure.step("Business Flow: Add New Task To The List")
    def add_new_task(task_name: str):
        UIActions.update_text(page.to_do_main.get_create_field(), task_name)
        UIActions.press_key(page.to_do_main.get_create_field(), Keys.ENTER)

    @staticmethod
    @allure.step("Business Flow: Count And Return Number Of Tasks In List")
    def get_number_of_tasks():
        return len(page.to_do_main.get_tasks_list())

    @staticmethod
    @allure.step("Business Flow: empty Lists From Tasks")
    def empty_list():
        for i in range(ElectronFlows.get_number_of_tasks()):
            UIActions.mouse_hover(page.to_do_main.get_x_btn())

    @staticmethod
    @allure.step("Business Flow: RGB Header Colors")
    def rgb_colors(r: str, g: str, b: str):
        equal = False
        UIActions.click(page.to_do_main.get_editor_header_btn())
        UIActions.click(page.to_do_main.get_header_colors_btn()[6])
        bg_color = page.to_do_main.get_bg_header_btn().get_attribute("style").split('(')[1]
        red = bg_color.split(",")[0]
        green = bg_color.split(",")[1]
        blue = bg_color.split(",")[2].split(')')[0]

        if r == red.strip() and g == green.strip() and b == blue.strip():
            equal = True

        return equal

    @staticmethod
    @allure.step("Business Flow: Mark Task Complete")
    def completed_task():
        UIActions.mouse_hover(page.to_do_main.get_v_list_btn()[0])
        UIActions.click(page.to_do_drawer.get_open_drawer_btn())
        UIActions.click(page.to_do_drawer.get_status_drawer_btn()[1])
