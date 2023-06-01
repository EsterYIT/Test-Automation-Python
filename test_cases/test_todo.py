import allure
import pytest
import utilities.manage_pages as page
from extensions.verifications import Verifications
from work_flows.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_electron_driver')
class TestElectron:

    @allure.title("Test01 - Add And Verify New Task")
    @allure.description("This test adds a new task and verifies it in the list task")
    def test01_add_and_verify_new_task(self):
        ElectronFlows.add_new_task("Learn Java")
        Verifications.number_of_elements(page.to_do_main.get_tasks_list(), 1)

    @allure.title("Test02 - Change Header Color")
    @allure.description("This test verifies that header color has been changed to the selected color by RGB")
    def test02_change_header_color(self):
        result = ElectronFlows.rgb_colors("189", "16", "224")
        assert result

    @allure.title("Test03 - Mark Task In 'V' And Verify That Task Is Not In Todo Tasks List")
    @allure.description("This test verifies that completed tasks is not shown in 'Todo' tasks list")
    def test03_mark_completed_tasks(self):
        ElectronFlows.add_new_task("Python")
        ElectronFlows.completed_task()
        Verifications.number_of_elements(page.to_do_main.get_tasks_list(), 1)


