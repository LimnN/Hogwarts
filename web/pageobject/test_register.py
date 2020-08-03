from web.pageobject.homepage import HomePage


class TestRegister(object):
    def setup(self):
        self.homepage = HomePage()

    def test_register(self):
        result = self.homepage.to_register().register()
        assert result == '请扫码进行管理员微信绑定'
