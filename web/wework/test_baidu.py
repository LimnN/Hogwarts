from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test:
    def setup_method(self):
        chrome_option = Options()
        chrome_option.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(chrome_options=chrome_option)

    def test_baidu(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.ID, 'kw').send_keys('Hogwarts')
        self.driver.find_element(By.ID, 'su').click()

    def test_cookie(self):

