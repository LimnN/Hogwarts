from selenium.webdriver.chrome.webdriver import WebDriver


class MessageBroadcast(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
