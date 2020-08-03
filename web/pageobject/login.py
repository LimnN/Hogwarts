from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from web.pageobject.register import Register


class Login(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def scan_login(self):
        pass

    def to_homepage(self):
        pass

    def to_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
