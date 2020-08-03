from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json


class Test:
    def setup_method(self):
        chrome_option = Options()
        chrome_option.debugger_address = '127.0.0.1:9222'
        self.cookies = json.load(open('cookie.json', 'r'))
        # self.driver = webdriver.Chrome(chrome_options=chrome_option)
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('Hogwarts')
        self.driver.find_element(By.ID, 'su').click()

    def test_cookie(self):
        self.driver.get('https://work.weixin.qq.com/')
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
