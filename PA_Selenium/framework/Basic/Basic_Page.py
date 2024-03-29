import os.path
from framework.Basic.Basic_Locator import basic_loc
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from framework.config import *


class BasicPage:
    """ This is a class for basic page """

    def __init__(self, driver, file):
        self.driver = driver
        self.verify_count = 0
        self.file = file
        self.browser = browser

    def find_display_element(self, locator):
        """ Wait 30 seconds until the element is visible """
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

    def find_display_elements(self, locators):
        """ Wait 30 seconds until the elements are visible """
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(locators))

    def cannot_find_display_element(self, locator):
        """ Wait 30 seconds until the elements are invisible """
        return WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located(locator))

    def search(self, keyword):
        """ Search items on the list page """
        self.find_display_element(basic_loc.input_search).clear()
        self.find_display_element(basic_loc.input_search).send_keys(keyword)
        self.find_display_element(basic_loc.input_search).send_keys(Keys.ENTER)
        sleep(1)

    def get_alert_message(self):
        """ Get the alert message """
        return self.find_display_element(basic_loc.alert_dialog).text

    def confirm(self):
        """ Click "Confirm" button """
        self.find_display_element(basic_loc.btn_confirm).click()
        sleep(1)

    def cancel(self):
        self.find_display_element(basic_loc.btn_cancel).click()
        sleep(1)

    def screenshot(self):
        """ Take a screenshot. """
        case = os.path.basename(self.file).split('.')[0].split('_')[1] + '_' + self.browser
        case_path = os.path.join(result_path, case)
        # Create results folder
        if not os.path.exists(case_path):
            os.mkdir(case_path)
        # Take a screenshot and save it in the results folder
        self.driver.save_screenshot(os.path.join(case_path, f'{case}_{self.verify_count}.png'))

    def assert_equal(self, actual, expect, is_take=True, msg=''):
        """ Verify whether actual value is equal to expected value.
            Take a screenshot before verification, by default.
            When is_take is False, screenshot won't be taken. """
        if msg == '':
            msg = f'\n\tActual: {actual}\n\tExpected: {expect}'
        assert actual == expect, msg
        if is_take:
            self.verify_count += 1
            self.screenshot()
