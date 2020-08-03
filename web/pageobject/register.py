from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def to_homepage(self):
        # self.driver.find_element(By.CSS_SELECTOR, '.ww_commonImg ww_commonImg_LogoSmall').click()
        # return HomePage()
        pass

    def register(self):
        corp = self.driver.find_element(By.ID, 'corp_name')
        corp.send_keys('Hogwarts')
        industry = self.driver.find_element(By.XPATH, '//*[@id="corp_industry"]/a').click()
        industry_select1 = self.driver.find_element(By.XPATH, '//*[@id="corp_industry"]/div/table/tbody/tr/td[1]/div[1]/a')
        industry_select1.click()
        industry_select2 = self.driver.find_element(By.XPATH, '//*[@id="corp_industry"]/div/table/tbody/tr/td[2]/div[1]/div[1]/a')
        industry_select2.click()
        scale = self.driver.find_element(By.XPATH, '//*[@id="corp_scale_btn"]').click()
        scale_select = self.driver.find_element(By.XPATH, '//*[@id="corp_scale_btn"]/div/ul/li[1]').click()
        admin = self.driver.find_element(By.XPATH, '//*[@id="manager_name"]')
        admin.send_keys('test')
        phone = self.driver.find_element(By.XPATH, '//*[@id="register_tel"]')
        phone.send_keys('12345678901')
        vcode = self.driver.find_element(By.XPATH, '//*[@id="vcode"]')
        vcode.send_keys('123456')
        agree = self.driver.find_element(By.XPATH, '//*[@id="iagree"]')
        agree.click()
        register = self.driver.find_element(By.XPATH, '//*[@id="submit_btn"]')
        register.click()

        notice = self.driver.find_element(By.XPATH, '//*[@id="js_tips"]')
        print(notice.get_attribute('innerText'))
        return notice.get_attribute('innerText')
