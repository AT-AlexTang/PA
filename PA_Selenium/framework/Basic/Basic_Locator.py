from framework.config import *


class BasicLocator:
    """ Element locators on basic page """
    alert_dialog = (xpath, "//div[@role='alertdialog']")
    input_search = (xpath, "//input[@data-placeholder='Search']")
    first_item = (xpath, "(//span//a)[1]")
    btn_confirm = (xpath, "//button[.='Confirm']")
    btn_cancel = (xpath, "//button[.='Cancel']")


basic_loc = BasicLocator()
