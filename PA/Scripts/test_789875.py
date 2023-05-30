from framework.DataConnectorPage import *


def test_789875(setup):
    """ PA-DCDP: UC746983 Edit Data Connector - Successful Save of an edited Data Connector """

    driver = setup
    dc_page = DataConnectorPage(driver, __file__)

    print('1. Go to Data Connectors list page')
    dc_page.open()

    print('2. Create a new Data Connector and input URL, Connector Type, Method, Headers and Parameters')
    name = 'DC_' + str(round(time() * 1000))
    URL = '123'
    Type = 'RESTFUL'
    method = 'GET'
    headers = [['K1', 'V1'], ['K2', 'V2']]
    params = [['K1', 'V1'], ['K2', 'V2']]

    # Create a new Data Connector
    dc_page.add_dc(name)

    # Add more detailed information
    dc_page.add_info(URL, Type, method, headers, params)

    print('3. Reopen the created Data Connector. Modify its detailed information and check whether modification can be saved successfully')
    URL = 'http://www.test.test'
    Type = 'GRAPHQL'
    method = 'QUERY'
    query = 'Test Query-1'
    headers = [['Test Key-1', 'Test Value-1'], ['Test Key-2', 'Test Value-2']]
    params = [['Test Key-1', 'Test Value-1'], ['Test Key-2', 'Test Value-2']]

    # Reopen the created Data Connector detail page
    dc_page.open_dc(name)

    # Modify its detailed information
    name = 'DC _.-:' + str(round(time() * 1000))
    dc_page.edit_all_info(name, URL, Type, method, headers, params, query)

    # Reopen and check whether the information is correct or not
    dc_page.open_dc(name)
    dc_page.verify_dc_detail(name, URL, Type, method, headers, params, query)

    # Delete the test data
    dc_page.delete_dc()
