import pytest
from mobile.pages.basepage import BasePage


class TestContact(object):
    def setup(self):
        self.base_page = BasePage()
        # self.base_page = BasePage(self.driver)

    def test_add_member(self):
        self.base_page.to_contacts().add_member()

        # self.base_page.to_contacts().add_member()
    def test_delete_member(self):
        self.base_page.to_contacts().delete_member()


if __name__ == '__main__':
    pytest.main(['--alluredir=./reports/results/'])
