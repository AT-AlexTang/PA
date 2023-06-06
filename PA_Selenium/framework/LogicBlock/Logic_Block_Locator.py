from framework.config import *


class LogicBlockListLocator:
    """ Element locators on Logic Blocks list page """
    menu_panel = (xpath, "//span[text()='Logic Blocks']")
    input_name = (xpath, '//textarea')
    first_name = (xpath, "(//div[@col-id='name'])[2]")
    first_type = (xpath, "(//div[@col-id='type'])[2]")
    btn_add = (css, '#add')
    btn_confirm = (xpath, "//button[.='check_box']")
    btn_delete = (xpath, "//button[.='delete']")
    select_type = (xpath, '//mat-select')
    option = '//mat-option'
    option_assignment = (xpath, "//mat-option[.=' assignment ']")


lb_list_loc = LogicBlockListLocator()
