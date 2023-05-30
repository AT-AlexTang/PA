import os
from selenium.webdriver.common.by import By

browser = 'Chrome'
# browser = 'Edge'

url = 'http://pa-frontend-qe.eastus.azurecontainer.io'
username = 'demo'
password = 'demo'

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
result_path = os.path.join(root_path, 'results')

xpath = By.XPATH
css = By.CSS_SELECTOR
