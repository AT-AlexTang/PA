from framework.config import *


class DataConnectorListLocator:
    """ Element locators on Data Connectors list page """
    menu_panel = (xpath, "//span[text()='Data Connectors']")
    input_name = (xpath, '//textarea')
    btn_add = (xpath, "//button[@type='button']")
    btn_ok = (xpath, "//button[.='check_box']")
    btn_delete = (xpath, "//button[.='delete']")


class DataConnectorDetailLocator:
    """ Element locators on Data Connector detail page """
    input_detail_name = (xpath, "//input[@formcontrolname='connectorName']")
    input_URL = (xpath, "//input[@formcontrolname='url']")
    input_query = (xpath, "//textarea")
    select_type = (xpath, "//mat-select[@formcontrolname='connectorType']")
    select_method = (xpath, "//mat-select[@formcontrolname='method']")
    option = '//mat-option'
    option_RESTFUL = (xpath, "//mat-option[.='RESTFUL']")
    option_GET = (xpath, "//mat-option[.='GET']")
    table = (css, '.ag-center-cols-viewport')
    tab_headers = (xpath, "//div[text()='Headers']")
    tab_params = (xpath, "//div[text()='Parameters']")
    input_key = (xpath, "//div[@role='gridcell' and @col-id='key']//input")
    input_value = (xpath, "//div[@role='gridcell' and @col-id='value']//input")
    btn_save = (xpath, "//button[@type='submit']")
    btn_cancel = (xpath, "//button[contains(.,'cancelCancel')]")
    btn_detail_delete = (css, ".delete-button-general")
    btn_endpoint = (css, ".btn-endpoint")
    btn_detail_add = (xpath, "//button[.='add']")
    btn_action_save = (css, ".table-icon-save")
    btn_action_edit = (css, ".table-icon-edit")
    btn_action_delete = (css, ".table-icon-delete")


dc_list_loc = DataConnectorListLocator()
dc_detail_loc = DataConnectorDetailLocator()
