import pytest

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_search_page()

    @pytest.mark.parametrize('key, stock_type, price', [
        ('阿里', '09988', 150)
    ])
    def test_search(self, key, stock_type, price):
        assert price < self.search.search(key).get_price(stock_type)

    def test_add_follow(self):
        self.search.search('阿里').add_follow('09988').get_follow_msg('09988')

    def test_market_quotations_add_follow(self):
        # 进入行情-点击搜索-添加自选-返回
        self.search.search('阿里')

    def teardown(self):
        pass
