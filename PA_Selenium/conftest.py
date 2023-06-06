import os.path
import pytest
from selenium import webdriver
from framework.Login.Login_Page import *
from framework.config import *


@pytest.fixture(scope='session', autouse=True)
def setup():
    # Create results folder for screenshots
    if not os.path.exists(result_path):
        os.mkdir(result_path)

    # Switch the test browser according to config.py
    if browser == 'Edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Edge(options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(options=options)

    # Open browser and login
    login_page = LoginPage(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    print('\n======== Start test case ========\n')
    login_page.login()
    yield driver
    print('\n======== End test case ========')
    driver.quit()
