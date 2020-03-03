import string

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class Search(BasePage):

    _search_input_locator = (MobileBy.ID, 'search_input_text')
    _stock_btn_locator = (
        MobileBy.XPATH, '//*[contains(@resource-id, "title_container")]/android.widget.TextView[@text="股票"]')

    def search(self, key: string):
        # 搜索指定内容
        self.find(self._search_input_locator).clear()
        self.find(self._search_input_locator).send_keys(key)
        # 点击第一条搜索结果
        self.find(MobileBy.ID, 'name').click()

        return self

    def search_close(self):
        self.find(MobileBy.ID, 'action_close').click()
        return self

    def get_price(self, key: string) -> float:
        stock_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "title_container")]/android.widget.TextView[@text="股票"]')
        hk_price_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "stockCode") and @text="%s"]/../../..//*[contains(@resource-id, "current_price")]' % key)

        # 点击股票分类
        self.find(stock_btn_locator).click()
        # 获取香港上市的阿里巴巴股票price
        price_element = self.find(hk_price_locator)
        price = float(price_element.get_attribute('text'))
        return price

    def add_follow(self, stock_type):
        follow_btn_locator = (MobileBy.XPATH,
                               '//*[contains(@resource-id, "stockCode") and @text="%s"]/../../..//*[contains(@resource-id, "follow_btn")]' % stock_type)

        # 点击股票分类
        self.find(self._stock_btn_locator).click()
        # 点击加自选按钮
        self.find(follow_btn_locator).click()

        return self

    def get_follow_msg(self):
        followed_btn_locator = (MobileBy.XPATH,
                                 '//*[contains(@resource-id, "stockCode") and @text="%s"]/../../..//*[contains(@resource-id, "followed_btn")]' % stock_type)

        # 点击股票分类
        self.find(self._stock_btn_locator).click()
        # 获取元素的所有attribute中text
        followed_btn_text = self.find(followed_btn_locator).get_attribute('text')

        return followed_btn_text
