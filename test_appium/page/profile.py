from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class Profile(BasePage):

    _password_login_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "rl_login")]/android.widget.TextView[@text="帐号密码登录"]')
    _account_input_locator = (MobileBy.ID, 'login_account')
    _password_input_locator = (MobileBy.ID, 'login_password')
    _login_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "button_next") and @text="登录"]')

    _alert_content_locator = (MobileBy.ID, 'md_content')
    _alert_close_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "md_buttonDefaultPositive") and @text="确定"]')

    def login_by_password(self, account, password):
        self.find(self._password_login_btn_locator).click()
        self.find(self._account_input_locator).send_keys(account)
        self.find(self._password_input_locator).send_keys(password)
        self.find(self._login_btn_locator).click()

        return_element = self.find(self._alert_locator)
        msg = return_element.get_attribute('text')
        self.find(self._alert_close_btn_locator).click()

        return msg
