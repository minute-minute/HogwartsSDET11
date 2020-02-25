from test_selenium.page.index import Index


class TestIndex:
    def setup_class(self):
        self.index = Index()

    def test_register(self):
        data = {
            'crop_name': 'test'
        }
        register_page = self.index.goto_register()
        register_page.register(data)
        assert '请选择' in register_page.get_error_message()

    def test_login(self):
        data = {
            'crop_name': 'test'
        }
        self.index.goto_login().goto_register().register(data)
