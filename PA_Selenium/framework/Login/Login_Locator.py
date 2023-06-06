from framework.config import *


class LoginLocator:
    """ Element locators on Login page """
    input_username = (css, '#username')
    input_password = (css, '#mat-input-1')
    btn_login = (css, '#signInBtn')


login_loc = LoginLocator()
