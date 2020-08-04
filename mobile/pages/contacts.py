from appium.webdriver.webdriver import WebDriver


class Contacts(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="添加成员"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="手动输入添加"]').click()
        name = self.driver.find_element_by_id('com.tencent.wework:id/azh')
        name.send_keys('abc')
