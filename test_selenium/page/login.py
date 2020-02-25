from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register


class Login(BasePage):

    def scan_code(self):
        pass

    def goto_register(self):
        self.find((By.LINK_TEXT, '立即注册')).click()
        return Register(self._driver)
