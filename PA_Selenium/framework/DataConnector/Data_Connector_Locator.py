from framework.Basic.Basic_Locator import BasicLocator
from framework.config import *


class DataConnectorListLocator(BasicLocator):
    """ Element locators on Data Connectors list page """
    menu_panel = (xpath, "//span[text()='Data Connectors']")    # Menu panel of Data Connector
    input_name = (xpath, '//textarea')                          # Name input field when creating a new Data Connector
    btn_ok = (xpath, "//button[.='check_box']")                 # Confirm button when creating a new Data Connector
    btn_delete = (xpath, "//button[.='delete']")                # Delete button when creating a new Data Connector


class DataConnectorDetailLocator:
    """ Element locators on Data Connector detail page """
    btn_save = (xpath, "//button[@type='submit']")                              # Save button to save Data Connector
    btn_cancel = (xpath, "//button[contains(.,'cancelCancel')]")                # Cancel button to restore Data Connector
    btn_delete = (css, ".delete-button-general")                                # Delete button to delete Data Connector
    btn_endpoint = (css, ".btn-endpoint")                                       # Validate Endpoint button to validate Data Connector
    input_name = (xpath, "//input[@formcontrolname='connectorName']")           # Name input field
    input_URL = (xpath, "//input[@formcontrolname='url']")                      # URL input field
    input_query = (xpath, "//textarea")                                         # Query String's input field for GraphQL API
    select_type = (xpath, "//mat-select[@formcontrolname='connectorType']")     # Connector Type drop-down
    select_method = (xpath, "//mat-select[@formcontrolname='method']")          # Method drop-down
    option = '//mat-option'                                                     # Option of each drop-down
    option_RESTFUL = (xpath, "//mat-option[.='RESTFUL']")                       # Option - RESTFUL
    option_GET = (xpath, "//mat-option[.='GET']")                               # Option - GET
    table = (css, '.ag-center-cols-viewport')                                   # Table of Headers or Parameters
    tab_headers = (xpath, "//div[text()='Headers']")                            # Headers Tab
    tab_params = (xpath, "//div[text()='Parameters']")                          # Parameters Tab
    input_key = (xpath, "//div[@role='gridcell' and @col-id='key']//input")     # Key's input field when editing headers or parameters
    input_value = (xpath, "//div[@role='gridcell' and @col-id='value']//input")  # Value's input field when editing headers or parameters
    btn_add = (xpath, "//button[.='add']")                                      # + button to create a new header or parameter
    btn_table_edit = (css, ".table-icon-edit")                                 # Edit button to edit a header or parameter
    btn_table_delete = (css, ".table-icon-delete")                             # Delete button to delete a header or parameter
    btn_table_save = (css, ".table-icon-save")                                 # Save button to save a header or parameter


dc_list_loc = DataConnectorListLocator()
dc_detail_loc = DataConnectorDetailLocator()
