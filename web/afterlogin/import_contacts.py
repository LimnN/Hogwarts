from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ImportContacts(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def upload(self):
        pass

    def to_goback(self):
        self.driver.find_element(By.XPATH, '//*[@id="import_back_no_loading"]').click()

    def to_fill_template(self):
        pass
