import pytest
from selenium import webdriver
from utilities.log_utils import LogData
import os
import requests
from lib.api_details.api import APIRequest


@pytest.fixture(scope="function")
def driver_data():
    options = webdriver.ChromeOptions()
    downloads = os.path.join(os.getcwd(), "downloads")
    prefs = {"download.default_directory": downloads}
    logger = LogData.log_step()
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\\Users\\SAM ANITH SP\\Desktop\\Logitech - Assignment\\chromedriver_win32\\chromedriver.exe", options= options)
    yield driver, logger
    driver.quit()

@pytest.fixture(scope="function")
def logger():
    logger = LogData.log_step()
    yield logger

@pytest.fixture(scope="function")
def requests_session():
    request_session = requests.session()
    auth_token = APIRequest.generate_auth_token(request_session)['token']
    yield request_session, auth_token
    request_session.close()


# pytest HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Automation Framework Development'
    config._metadata['Module Name'] = 'SeleniumEasy'
    config._metadata['Developer'] = 'Anushiya'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
