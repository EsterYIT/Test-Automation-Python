import pytest
import allure
import selenium
import mysql.connector
import appium.webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.event_listener import EventListener
from utilities.common_ops import get_data
from utilities.manage_pages import ManagePages

driver = None
action = None
m_action = None
action2 = None
db_connector = None


@pytest.fixture()
def init_web_driver(request):
    if get_data('execute_app_tools').lower() == 'yes':
        globals()['driver'] = get_web_driver()
    else:
        edriver = get_web_driver()
        globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('waitTime')))
    driver.get((get_data('url')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_web_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('wait_time')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['m_action'] = TouchAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('wait_time')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('waitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_db_connection(request):
    edriver = get_web_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('wait_time')))
    driver.get((get_data('url')))
    ManagePages.init_web_pages()
    db_connector = mysql.connector.connect(
        host=get_data("DB_host"),
        database=get_data('DB_name'),
        user=get_data('DB_username'),
        port=get_data('DB_port'),
        password=get_data('DB_password')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    driver.quit()
    db_connector.close()


def get_web_driver():
    web_driver = get_data('browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong Input, Unrecognized Browser')
    return driver


def get_chrome():
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


def get_firefox():
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return ff_driver


def get_edge():
    edge_driver = selenium.webdriver.Edge(EdgeChromiumDriverManager().install())
    return edge_driver


def get_mobile_driver():
    if get_data('mobile_device').lower() == 'android':
        driver = get_android(get_data('UDID'))
    # elif get_data('Mobile_device').lower() == 'ios':
    #     driver = get_ios(get_data('Udid'))
    else:
        driver = None
        raise Exception('Wrong input, unrecognized mobile OS')
    return driver


def get_android(udid):
    dc={}
    dc['udid'] = udid
    dc['appPackage'] = get_data('app_package')
    dc['appActivity'] = get_data('app_activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('appium_server'), dc)
    return android_driver


def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('app_signature')
    dc['platformName'] = 'windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('desktop_url'), dc)
    return driver


def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data('electron_app_path')
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data('electron_driver_path'))
    return driver


def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:
            allure.attach(globals()['driver'].get_screenshot_as_png(), name="screenshot.png",
                          attachment_type=allure.attachment_type.PNG)