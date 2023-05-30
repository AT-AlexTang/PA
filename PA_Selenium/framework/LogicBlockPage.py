from framework.Page import *
from framework.config import *
from time import sleep
from time import time


class LogicBlockPage(Page):
    """ This is a class for logic blocks page """

    # Element locators on Logic Blocks page
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

    def __init__(self, driver, file=__file__):
        super().__init__(driver, file)

    def open(self):
        """ Go to Logic Blocks list page """
        self.find_element(self.menu_panel).click()
        sleep(1)

    def add(self, Type, name='LB_'+str(round(time()*1000))):
        """ Add a new logic block """
        self.find_element(self.btn_add).click()
        self.find_element(self.input_name).clear()
        self.find_element(self.input_name).send_keys(name)
        self.find_element(self.select_type).click()
        self.find_element((xpath, f"{self.option}[.=' {Type} ']")).click()
        self.find_element(self.btn_confirm).click()
