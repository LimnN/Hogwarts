from appium.webdriver.webdriver import WebDriver

from mobile.device_connect import Device
from mobile.pages.console import Console
from mobile.pages.contacts import Contacts


class Message(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def to_console(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="工作台"]').click()
        return Console(self.driver)

    def to_contacts(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="通讯录"]').click()
        return Contacts(self.driver)


if __name__ == '__main__':
    device = Device()
    wework = Message(device.driver)
    wework.to_contacts().add_member()
