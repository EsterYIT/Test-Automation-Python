
import test_cases.conftest as conf
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
import time
import csv

"""
    Method Name: read_data_from_csv
    Method Description: This method get the data from csv file
    Method Parameters: String
    Method Return: List
"""


def read_data_from_csv(csv_file_path):
    data_list = []
    # open csv file
    csv_data = open(csv_file_path, 'r')
    # create csv reader object
    reader = csv.reader(csv_data)
    # skip header
    next(reader)
    # add csv data to list
    for row in reader:
        data_list.append(row)

    return data_list


"""
    Method Name: get_data
    Method Description: This method get the data from xml configuration file
    Method Parameters: String
    Method Return: String
"""


def get_data(node_name):
    root = ET.parse('C:/python-selenium/FinalProject/configuration/config.xml').getroot()
    return root.find('.//' + node_name).text


def get_time_stamp():
    return time.time()


def wait_for_presence_of_all_elements(elements):
    wait = WebDriverWait(conf.driver, int(get_data("wait_time")))
    wait.until(EC.presence_of_all_elements_located(elements))


def wait_until_element_is_clickable(elem):
    wait = WebDriverWait(conf.driver, int(get_data("wait_time")))
    wait.until(EC.visibility_of(elem))


def wait_until_element_is_located(elem):
    wait = WebDriverWait(conf.driver, int(get_data("wait_time")))
    wait.until(EC.presence_of_element_located(elem))


def wait_until_element_is_visible(elem):
    wait = WebDriverWait(conf.driver, int(get_data("wait_time")))
    wait.until(EC.visibility_of(elem))


# Enum for selecting direction to swipe in mobile tests
class Direction:
    Left = 'left'
    Right = 'right'
    UP = 'up'
    DOWN = 'down'
