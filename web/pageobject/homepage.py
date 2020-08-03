from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from web.pageobject.login import Login
from web.pageobject.register import Register


class HomePage(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver if driver is not None else webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        # self.driver = webdriver.Chrome()

    def to_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

    def to_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self.driver)


if __name__ == '__main__':
    home = HomePage()
    home.to_register().register()
