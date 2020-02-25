from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def download_app(self):
        pass

    def import_user(self):
        # upload file of excel
        pass

    def goto_company(self):
        pass

    def show_message(self):
        return True

    def add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        self.find(locator).click()
        # self._driver.execute_script('arguments[0].click();', self.find(locator))
        return Contact(reuse=True)

    def send_message(self, data):
        pass
