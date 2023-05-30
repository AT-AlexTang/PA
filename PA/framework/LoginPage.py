from framework.Page import *
from framework.config import *


class LoginPage(Page):
    """ This is a class for login page """

    # Element locators on Login page
    input_username = (css, '#username')
    input_password = (css, '#mat-input-1')
    btn_login = (css, '#signInBtn')

    def __init__(self, driver, file=__file__):
        super().__init__(driver, file)

    def login(self):
        """ Login the website. """
        self.driver.get(url + '/login')
        self.find_element(self.input_username).send_keys(username)
        self.find_element(self.input_password).send_keys(password)
        self.find_element(self.btn_login).click()
