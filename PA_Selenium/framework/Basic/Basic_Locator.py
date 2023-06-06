from framework.config import *


class BasicLocator:
    """ Element locators on basic page """
    alert_dialog = (xpath, "//div[@role='alertdialog']")            # Alert message dialog
    input_search = (xpath, "//input[@data-placeholder='Search']")   # Search bar
    first_item = (xpath, "(//span//a)[1]")                          # The first item in the list
    btn_add = (xpath, "//button[@type='button']")                   # + button to create a new item
    btn_confirm = (xpath, "//button[.='Confirm']")                  # Confirm button on the warning message dialog
    btn_cancel = (xpath, "//button[.='Cancel']")                    # Cancel button on the warning message dialog


basic_loc = BasicLocator()
