from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.search import Search


class Market(BasePage):
    _search_locator = (MobileBy.ID, 'action_search')

    def goto_search_page(self):
        self.find(self._search_locator).click()
        return Search(self._driver)

