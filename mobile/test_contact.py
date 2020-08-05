import pytest
from appium.webdriver.webdriver import WebDriver
from mobile.device_connect import Device
from mobile.pages.basepage import BasePage


class TestContact(object):
    def setup(self, driver: WebDriver):
        self.driver = Device().driver
        # self.base_page = BasePage(self.driver)

    def test_add_member(self):
        base_page = BasePage(self.driver)

        # self.base_page.to_contacts().add_member()


if __name__ == '__main__':
    pytest.main()
