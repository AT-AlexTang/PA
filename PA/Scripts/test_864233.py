from framework.LogicBlockPage import *


def test_864233(setup):
    """ PA-BLB: UC753118 - Basic Logic Builder - Series - Dismiss sign """

    driver = setup
    logic_block_page = LogicBlockPage(driver, __file__)

    print('1. Go to Logic Blocks page')
    logic_block_page.open()

    print('2. Add a new logic block')
    name = 'LB_' + str(round(time() * 1000))
    logic_block_page.find_element(logic_block_page.btn_add).click()
    logic_block_page.find_element(logic_block_page.input_name).clear()
    logic_block_page.find_element(logic_block_page.input_name).send_keys(name)
    logic_block_page.find_element(logic_block_page.select_type).click()
    options = [locator.text for locator in logic_block_page.find_elements((xpath, logic_block_page.option))]

    print('3. Verify the name and type of logic block')
    logic_block_page.assert_equal(options[0], 'assignment')
    logic_block_page.assert_equal(options[1], 'condition', 0)
    logic_block_page.assert_equal(options[2], 'conditional assignment', 0)
    logic_block_page.find_element(logic_block_page.option_assignment).click()
    sleep(1)
    actual_name = logic_block_page.find_element(logic_block_page.first_name).text
    actual_type = logic_block_page.find_element(logic_block_page.first_type).text
    logic_block_page.assert_equal(actual_name, name)
    assert 'assignment' in actual_type
    logic_block_page.find_element(logic_block_page.btn_delete).click()
