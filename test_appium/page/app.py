from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


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
        return Main(self._driver)
