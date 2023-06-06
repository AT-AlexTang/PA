from framework.Basic.Basic_Page import *
from framework.LogicBlock.Logic_Block_Locator import lb_list_loc
from framework.config import *
from time import sleep
from time import time


class LogicBlockBasicPage(BasicPage):
    """ This is a class for logic blocks page """

    def __init__(self, driver, file=__file__):
        super().__init__(driver, file)

    def open(self):
        """ Go to Logic Blocks list page """
        self.find_display_element(lb_list_loc.menu_panel).click()
        sleep(1)

    def add(self, Type, name='LB_'+str(round(time()*1000))):
        """ Add a new logic block """
        self.find_display_element(lb_list_loc.btn_add).click()
        self.find_display_element(lb_list_loc.input_name).clear()
        self.find_display_element(lb_list_loc.input_name).send_keys(name)
        self.find_display_element(lb_list_loc.select_type).click()
        self.find_display_element((xpath, f"{lb_list_loc.option}[.=' {Type} ']")).click()
        self.find_display_element(lb_list_loc.btn_ok).click()
