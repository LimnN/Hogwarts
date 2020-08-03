from selenium.webdriver.chrome.webdriver import WebDriver


class CustomContact(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
