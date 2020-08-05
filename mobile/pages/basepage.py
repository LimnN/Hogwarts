from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from mobile.pages.console import Console
from mobile.pages.contacts import Contacts
from mobile.pages.me import Me
from mobile.pages.message import Message


class BasePage(object):
    def __init__(self, driver: WebDriver):
        ANDROID_BASE_CAPS = {
            # 'app': os.path.abspath('../app/wework_3_0_27.apk'),
            'automationName': 'UIAutomator2',
            'platformName': 'Android',
            'platformVersion': '11.0',
            'deviceName': '9A241FFBA00003',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'noReset': True,
            # 'skipServerInstallation': True,
            # 'skipDeviceInitialization': True
        }

        EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

        self.driver = webdriver.Remote(command_executor=EXECUTOR, desired_capabilities=ANDROID_BASE_CAPS)
        self.driver.implicitly_wait(5)

    def to_message(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="消息"]').click()
        return Message(self.driver)

    def to_contacts(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="通讯录"]').click()
        return Contacts(self.driver)

    def to_console(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="工作台"]').click()
        return Console(self.driver)

    def to_me(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="我"]').click()
        return Me(self.driver)
