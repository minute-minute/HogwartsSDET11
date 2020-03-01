from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.profile import Profile
from test_appium.page.search import Search


class Main(BasePage):
    _search_locator = (MobileBy.ID, 'tv_search')
    _profile_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "tab_name") and @text="我的"]')

    def goto_search_page(self):
        self.find(self._search_locator).click()
        return Search(self._driver)

    def goto_stocks(self):
        pass

    def goto_profile(self):
        self.find(self._profile_locator).click()
        return Profile(self._driver)
