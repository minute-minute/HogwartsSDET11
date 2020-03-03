import time
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):
        self.__init_app()

        # 常用元素
        self.__search_locator = (MobileBy.ID, 'tv_search')
        self.__search_input_locator = (MobileBy.ID, 'search_input_text')

    def __init_app(self):
        caps = {}
        caps['deviceName'] = 'xu'
        caps['platformName'] = 'Android'
        caps['appPackage'] = 'io.appium.android.apis'
        caps['appActivity'] = '.ApiDemos'

        # 重置数据
        # caps['noReset'] = True
        # 不关闭app
        # caps['dontStopAppOnReset'] = True
        # # 使用中文
        # caps['unicodeKeyboard'] = True
        # # 重置键盘
        # caps['resetKeyboard'] = True
        # 初始安装就可
        # caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def find(self, by, value=None) -> WebElement:
        if isinstance(by, tuple):
            return self.driver.find_element(*by)
        return self.driver.find_element(by, value)

    def test_scroll(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0)'
            ').scrollIntoView('
                'new UiSelector().text("Views").instance(0)'
            ');'
        )
        self.find(*scroll_to_element).click()
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0)'
            ').scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0)'
            ');'
        )
        self.find(*scroll_to_element).click()
        # ACCESSIBILITY_ID对应content-desc
        self.find(MobileBy.ACCESSIBILITY_ID, 'Make a Popup!').click()
        self.find(MobileBy.XPATH, '//*[@text="Search"]').click()
        toast = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text

        assert 'Clicked' in toast
        assert 'Search' in toast

    def teardown(self):
        # pass
        time.sleep(10)
        self.driver.quit()
