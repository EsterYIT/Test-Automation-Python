import test_cases.conftest as conf
from page_objects.calculator.main_page import CalculatorPage
from page_objects.db_conduit.menu_head_page import MenuHead
from page_objects.db_conduit.sign_in_page import SignInPage
from page_objects.db_conduit.user_head_page import UserHead
from page_objects.grafana.admin_main_page import AdminMainPage
from page_objects.grafana.admin_menu_page import AdminMenuPage
from page_objects.grafana.left_menu_page import LeftMenuPage
from page_objects.grafana.login_page import LoginPage
from page_objects.grafana.main_page import MainPage
from page_objects.grafana.create_new_user_page import CreateNewUser
from page_objects.grafana.new_user_main_page import NewUserMainPage
from page_objects.todo.drawer_page import ToDoDrawer
from page_objects.todo.main_page import ToDoMain
from page_objects.uk_mortgage.main_page import MainPageMortgage

# Web Objects
web_login = None
web_main = None
web_left_menu = None
web_admin_menu_page = None
web_admin_main_page = None
web_create_new_user = None
web_new_user_page = None
db_web_conduit_menu_head = None
db_web_conduit_sign_in = None
db_web_conduit_user_head = None

# Mobile Objects
mobile_mortgage_main = None

# Desktop Objects
desktop_main = None

# Electron Objects
to_do_main = None
to_do_drawer = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_left_menu'] = LeftMenuPage(conf.driver)
        globals()['web_admin_menu_page'] = AdminMenuPage(conf.driver)
        globals()['web_admin_main_page'] = AdminMainPage(conf.driver)
        globals()['web_create_new_user'] = CreateNewUser(conf.driver)
        globals()['web_new_user_page'] = NewUserMainPage(conf.driver)

        # DB Conduit Sign In
        globals()['db_web_conduit_menu_head'] = MenuHead(conf.driver)
        globals()['db_web_conduit_sign_in'] = SignInPage(conf.driver)
        globals()['db_web_conduit_user_head'] = UserHead(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_mortgage_main'] = MainPageMortgage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['desktop_main'] = CalculatorPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['to_do_main'] = ToDoMain(conf.driver)
        globals()['to_do_drawer'] = ToDoDrawer(conf.driver)
