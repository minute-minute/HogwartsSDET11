from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main
import logging


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'

    def start(self):
        caps = dict()
        caps['deviceName'] = 'xu'
        caps['platformName'] = 'Android'
        caps['appPackage'] = self._package
        caps['appActivity'] = self._activity

        # 重置数据
        caps['noReset'] = True
        # 不关闭app
        caps['dontStopAppOnReset'] = True
        # 使用中文
        caps['unicodeKeyboard'] = True
        # 重置键盘
        caps['resetKeyboard'] = True
        # 初始安装就可
        caps['skipServerInstallation'] = True

        if self._driver is None:
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        else:
            self._driver.start_activity(self._package, self._activity)

        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        return self

    def stop(self):
        return self

    def main(self):
        def is_loaded(driver):
            loaded_tag = ['同意', '我的']
            source = self._driver.page_source
            for tag in loaded_tag:
                if tag in source:
                    return True

                if loaded_tag[-1] == tag:
                    return False

            return True

        logging.info('wait main page init.')
        # wait main page init
        WebDriverWait(self._driver, 30).until(is_loaded)
        return Main(self._driver)
