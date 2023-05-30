from framework.Page import *
from framework.config import *
from time import sleep
from time import time


class DataConnectorPage(Page):
    """ This is a class for Data Connectors page """

    # Element locators on Data Connectors page
    menu_panel = (xpath, "//span[text()='Data Connectors']")
    input_name = (xpath, '//textarea')
    btn_add = (xpath, "//button[@type='button']")
    btn_ok = (xpath, "//button[.='check_box']")
    btn_delete = (xpath, "//button[.='delete']")

    # Element locators on DC detail page
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
    btn_detail_confirm = ()

    def open(self):
        """ Go to Data Connectors page """
        self.find_element(self.menu_panel).click()
        sleep(1)
    
    def open_dc(self, name):
        """ Open the specific Data Connector detail page """
        self.open()
        self.search(name)
        self.find_element(self.first_item).click()

    def add_dc(self, name='DC_'+str(round(time()*1000))):
        """ Add a new Data Connector """
        self.find_element(self.btn_add).click()
        self.find_element(self.input_name).clear()
        self.find_element(self.input_name).send_keys(name)
        self.find_element(self.btn_ok).click()

    def add_info(self, URL, Type, method, headers=None, params=None, query=None):
        """ Add URL, Connector Type, Method, Query String for GraphQL, Headers and Parameters on the detail page """
        # Input URL
        self.find_element(self.input_URL).clear()
        self.find_element(self.input_URL).send_keys(URL)
        # Choose Connector type
        self.find_element(self.select_type).click()
        self.find_element((xpath, f"{self.option}[.='{Type}']")).click()
        # Choose Method if Connector type is RESTFUL or GRAPHQL
        if Type == 'RESTFUL' or 'GRAPHQL':
            self.find_element(self.select_method).click()
            self.find_element((xpath, f"{self.option}[.='{method}']")).click()
            # Input query string if Connector type is GRAPHQL
            if Type == 'GRAPHQL':
                self.find_element(self.input_query).send_keys(query)
        # Add Headers
        for index, header in enumerate(headers):
            self.find_element(self.btn_detail_add).click()
            self.find_element(self.input_key).send_keys(header[0])
            self.find_element(self.input_value).send_keys(header[1])
            self.find_element(self.btn_action_save).click()
            sleep(0.5)
        # Add Parameters
        self.find_element(self.tab_params).click()
        sleep(1)
        for index, param in enumerate(params):
            self.find_element(self.btn_detail_add).click()
            self.find_element(self.input_key).send_keys(param[0])
            self.find_element(self.input_value).send_keys(param[1])
            self.find_element(self.btn_action_save).click()
            sleep(0.5)
        # Click "Save" button
        self.find_element(self.btn_save).click()
        self.assert_equal(self.get_alert_message(), 'Connector updated successfully', 0)

    def edit_all_info(self, name, URL, Type, method, headers=None, params=None, query=None):
        """ Edit name, URL, Connector Type, Method, Query String for GraphQL, Headers and Parameters on the detail page """
        # Edit Connector Name
        sleep(1)
        self.find_element(self.input_detail_name).clear()
        self.find_element(self.input_detail_name).send_keys(name)
        # Edit URL
        self.find_element(self.input_URL).clear()
        self.find_element(self.input_URL).send_keys(URL)
        # Edit Connector type
        self.find_element(self.select_type).click()
        self.find_element((xpath, f"{self.option}[.='{Type}']")).click()
        # Edit Method if Connector type is RESTFUL or GRAPHQL
        if Type == 'RESTFUL' or 'GRAPHQL':
            self.find_element(self.select_method).click()
            self.find_element((xpath, f"{self.option}[.='{method}']")).click()
            # Input query string if Connector type is GRAPHQL
            if Type == 'GRAPHQL':
                self.find_element(self.input_query).clear()
                self.find_element(self.input_query).send_keys(query)
        # Edit Headers
        btn_edits = [locator for locator in self.find_elements(self.btn_action_edit)]
        for index, header in enumerate(headers):
            btn_edits[index].click()
            self.find_element(self.input_key).clear()
            self.find_element(self.input_key).send_keys(header[0])
            self.find_element(self.input_value).clear()
            self.find_element(self.input_value).send_keys(header[1])
            self.find_element(self.btn_action_save).click()
            sleep(0.5)
        # Edit Parameters
        self.find_element(self.tab_params).click()
        sleep(1)
        btn_edits = [locator for locator in self.find_elements(self.btn_action_edit)]
        for index, param in enumerate(params):
            btn_edits[index].click()
            self.find_element(self.input_key).clear()
            self.find_element(self.input_key).send_keys(param[0])
            self.find_element(self.input_value).clear()
            self.find_element(self.input_value).send_keys(param[1])
            self.find_element(self.btn_action_save).click()
            sleep(0.5)
        # Click "Save" button
        self.find_element(self.btn_save).click()
        self.assert_equal(self.get_alert_message(), 'Connector updated successfully', 0)

    def verify_dc_detail(self, name, URL, Type, method, headers, params, query):
        """ Verify all information on the detail page """
        sleep(1)
        actual_name = self.find_element(self.input_detail_name).get_attribute('value')
        actual_URL = self.find_element(self.input_URL).get_attribute('value')
        actual_Type = self.find_element(self.select_type).text
        actual_method = self.find_element(self.select_method).text
        actual_query = self.find_element(self.input_query).get_attribute('value')
        self.assert_equal(actual_name, name)
        self.assert_equal(actual_URL, URL, 0)
        self.assert_equal(actual_Type, Type, 0)
        self.assert_equal(actual_method, method, 0)
        for index, header in enumerate(headers):
            actual_key = self.find_element((xpath, f"(//div[@col-id='key'])[{index+2}]")).text
            actual_value = self.find_element((xpath, f"(//div[@col-id='value'])[{index+2}]")).text
            actual_header = [actual_key, actual_value]
            self.assert_equal(actual_header, header, 0)
        self.find_element(self.tab_params).click()
        sleep(1)
        for index, param in enumerate(params):
            actual_key = self.find_element((xpath, f"(//div[@col-id='key'])[{index + 2}]")).text
            actual_value = self.find_element((xpath, f"(//div[@col-id='value'])[{index + 2}]")).text
            actual_param = [actual_key, actual_value]
            self.assert_equal(actual_param, param, 0)
        self.assert_equal(actual_query, query)
    
    def delete_dc(self):
        """ Click "Delete" button on the detail page """
        self.find_element(self.btn_detail_delete).click()
        self.confirm()
        self.find_element(self.input_search)
