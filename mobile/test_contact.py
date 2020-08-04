from appium.webdriver.webdriver import WebDriver
from mobile.device_connect import Device


class TestContact(object):
    def setup(self, driver: WebDriver):
        self.driver = Device()


if __name__ == '__main__':
    pass
