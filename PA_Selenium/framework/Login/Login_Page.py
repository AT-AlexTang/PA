from framework.Basic.Basic_Page import *
from framework.Login.Login_Locator import login_loc
from framework.config import *


class LoginPage(BasicPage):
    """ This is a class for login page """
    def __init__(self, driver, file=__file__):
        super().__init__(driver, file)

    def login(self):
        """ Login the website. """
        self.driver.get(url + '/login')
        self.find_display_element(login_loc.input_username).send_keys(username)
        self.find_display_element(login_loc.input_password).send_keys(password)
        self.find_display_element(login_loc.btn_login).click()
