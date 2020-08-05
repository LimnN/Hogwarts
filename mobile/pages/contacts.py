import time

from appium.webdriver.webdriver import WebDriver


class Contacts(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="添加成员"]').click()
        self.driver.find_element_by_id('com.tencent.wework:id/cgl').click()
        name = self.driver.find_element_by_xpath('//android.widget.EditText[@text="必填"]')
        name.send_keys('abc')
        self.driver.find_element_by_id('com.tencent.wework:id/e__').click()
        male = self.driver.find_element_by_xpath('//android.widget.TextView[@text="男"]')
        female = self.driver.find_element_by_xpath('//android.widget.TextView[@text="女"]').click()
        phone = self.driver.find_element_by_id('com.tencent.wework:id/f9s')
        phone.send_keys('12345678901')
        mail = self.driver.find_element_by_xpath('//android.widget.EditText[@text="选填"]')
        mail.send_keys('mymail@abc.com')
        address = self.driver.find_element_by_id('com.tencent.wework:id/id').click()
        add = self.driver.find_element_by_id('com.tencent.wework:id/ie')
        add.send_keys('my address1')
        self.driver.find_element_by_id('com.tencent.wework:id/hk6').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.wework:id/hkc').click()

    def delete_member(self):
        self.driver.find_element_by_xpath('//*[@text="abc"]').click()
        self.driver.find_element_by_id('com.tencent.wework:id/hjz').click()
        self.driver.find_element_by_id('com.tencent.wework:id/b53').click()
        self.driver.find_element_by_id('com.tencent.wework:id/e_1').click()
        self.driver.find_element_by_id('com.tencent.wework:id/bfe').click()
