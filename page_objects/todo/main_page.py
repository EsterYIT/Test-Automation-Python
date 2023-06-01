from selenium.webdriver.common.by import By

create_field = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks_list = (By.CLASS_NAME, "view_2Ow90")
x_btn = (By.CLASS_NAME, "destroy_19w1q")
header_colors_btn = (By.XPATH, "//div[@class='vc-sketch-presets']/div")
editor_header_btn = (By.XPATH, "//div[@class='icons_MDNeU']//*[name()='svg'][1]")
bg_header_btn = (By.XPATH, "//header[@class='wrapper_2r1C1']")
v_list_btn = (By.CLASS_NAME, "toggleIconsWrapper_2kpi8")
no_tasks_txt = (By.CLASS_NAME, "emptyState_3FwtK")


class ToDoMain:

    def __init__(self, driver):
        self.driver = driver

    def get_create_field(self):
        return self.driver.find_element(*create_field)

    def get_tasks_list(self):
        return self.driver.find_elements(*tasks_list)

    def get_x_btn(self):
        return self.driver.find_element(*x_btn)

    def get_header_colors_btn(self):
        return self.driver.find_elements(*header_colors_btn)

    def get_editor_header_btn(self):
        return self.driver.find_element(*editor_header_btn)

    def get_bg_header_btn(self):
        return self.driver.find_element(*bg_header_btn)

    def get_v_list_btn(self):
        return self.driver.find_elements(*v_list_btn)

    def get_no_tasks_txt(self):
        return self.driver.find_element(*no_tasks_txt)