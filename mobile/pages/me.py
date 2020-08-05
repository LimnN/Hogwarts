from appium.webdriver.webdriver import WebDriver


class Me(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
