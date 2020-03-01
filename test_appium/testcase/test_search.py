import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize('key, stock_type, price', [
        ('阿里', 'aaa', 150)
    ])
    def test_search(self, key, stock_type, price):
        assert price < self.main.goto_search_page().search(key).get_price(stock_type)

    def teardown(self):
        pass
