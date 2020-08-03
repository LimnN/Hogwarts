from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.afterlogin.add_member import AddMember
from web.afterlogin.checkin import Checkin
from web.afterlogin.custom_contact import CustomContact
from web.afterlogin.import_contacts import ImportContacts
from web.afterlogin.member_join import MemberJoin
from web.afterlogin.message_broadcast import MessageBroadcast


class Index(object):
    def __init__(self, driver: WebDriver = None):
        self.driver = driver if driver is not None else webdriver.Chrome()

    def to_add_member(self):
        xpath_click(self.driver, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')
        return AddMember(self.driver)

    def to_import_contacts(self):
        xpath_click(self.driver, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]')
        return ImportContacts(self.driver)

    def to_member_join(self):
        xpath_click(self.driver, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[3]')
        return MemberJoin(self.driver)

    def to_message_broadcast(self):
        xpath_click(self.driver, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[4]')
        return MessageBroadcast(self.driver)

    def to_custom_contact(self):
        xpath_click(self.driver, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[5]')
        return CustomContact(self.driver)

    def to_checkin(self):
        xpath_click(self.driver, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[6]')
        return Checkin(self.driver)


def xpath_click(driver: WebDriver, xpath):
    return driver.find_element(By.XPATH, xpath).click()


if __name__ == '__main__':
    index = Index()
    index.to_import_contacts().to_goback()
