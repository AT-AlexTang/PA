from framework.LogicBlock.Logic_Block_Page import *
from framework.LogicBlock.Logic_Block_Locator import lb_list_loc


def test_864233(setup):
    """ PA-BLB: UC753118 - Basic Logic Builder - Series - Dismiss sign """

    driver = setup
    logic_block_page = LogicBlockBasicPage(driver, __file__)

    print('1. Go to Logic Blocks page')
    logic_block_page.open()

    print('2. Add a new logic block')
    name = 'LB_' + str(round(time() * 1000))
    logic_block_page.find_display_element(lb_list_loc.btn_add).click()
    logic_block_page.find_display_element(lb_list_loc.input_name).clear()
    logic_block_page.find_display_element(lb_list_loc.input_name).send_keys(name)
    logic_block_page.find_display_element(lb_list_loc.select_type).click()
    options = [locator.text for locator in logic_block_page.find_display_elements((xpath, lb_list_loc.option))]

    print('3. Verify the name and type of logic block')
    logic_block_page.assert_equal(options[0], 'assignment')
    logic_block_page.assert_equal(options[1], 'condition', 0)
    logic_block_page.assert_equal(options[2], 'conditional assignment', 0)
    logic_block_page.find_display_element(lb_list_loc.option_assignment).click()
    sleep(1)
    actual_name = logic_block_page.find_display_element(lb_list_loc.first_name).text
    actual_type = logic_block_page.find_display_element(lb_list_loc.first_type).text
    logic_block_page.assert_equal(actual_name, name)
    assert 'assignment' in actual_type
    logic_block_page.find_display_element(lb_list_loc.btn_delete).click()
