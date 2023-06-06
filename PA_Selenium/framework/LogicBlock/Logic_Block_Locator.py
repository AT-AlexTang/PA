from framework.Basic.Basic_Locator import BasicLocator
from framework.config import *


class LogicBlockListLocator(BasicLocator):
    """ Element locators on Logic Blocks list page """
    menu_panel = (xpath, "//span[text()='Logic Blocks']")           # Menu panel of Logic Blocks
    input_name = (xpath, '//textarea')                              # Name input field when creating a new Logic Block
    first_name = (xpath, "(//div[@col-id='name'])[2]")              # Name of the first Logic Block
    first_type = (xpath, "(//div[@col-id='type'])[2]")              # Type of the first Logic Block
    btn_ok = (xpath, "//button[.='check_box']")                     # Confirm button when creating a new Logic Block
    btn_delete = (xpath, "//button[.='delete']")                    # Delete button when creating a new Logic Block
    select_type = (xpath, '//mat-select')                           # Logic Block Type drop-down when creating a new Logic Block
    option = '//mat-option'                                         # Option of Logic Block Type drop-down
    option_assignment = (xpath, "//mat-option[.=' assignment ']")   # Option - assignment


lb_list_loc = LogicBlockListLocator()
