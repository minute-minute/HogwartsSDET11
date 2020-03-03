from test_appium.page.app import App


class TestMarket:
    def setup(self):
        self.market = App().start().main().goto_market_quotations_page()

    def test_market_quotations_add_follow(self):
        # 进入行情-点击搜索-添加自选-返回
        self.market.goto_search_page().search('阿里').add_follow('09988').search_close()

    def teardown(self):
        pass
