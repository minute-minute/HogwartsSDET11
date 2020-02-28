import time
from appium import webdriver
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
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'

        # 重置数据
        # caps['noReset'] = True
        # 不关闭app
        caps['dontStopAppOnReset'] = True
        # 使用中文
        caps['unicodeKeyboard'] = True
        # 重置键盘
        caps['resetKeyboard'] = True
        # 初始安装就可
        # caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def find(self, by, value=None):
        if isinstance(by, tuple):
            return self.driver.find_element(*by)
        return self.driver.find_element(by, value)

    def test_search(self):
        time.sleep(40)
        # noReset=False时只在启动时会出现一次
        self.driver.find_element(MobileBy.ID, 'tv_agree').click()
        self.find(self.__search_locator).click()
        self.find(self.__search_input_locator).send_keys('阿里')

    def __search(self, content, first=True):
        # 再次搜索无该按钮
        if first:
            self.find(self.__search_locator).click()
        # 搜索指定内容
        self.find(self.__search_input_locator).clear()
        self.find(self.__search_input_locator).send_keys(content)
        # 点击第一条搜索结果
        self.find(MobileBy.ID, 'name').click()

    def test_search_and_get_target_price(self):
        stock_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "title_container")]/android.widget.TextView[@text="股票"]')
        hk_price_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "stockCode") and @text="09988"]/../../..//*[contains(@resource-id, "current_price")]')

        self.__search('阿里')
        # 点击股票分类
        self.find(stock_btn_locator).click()
        # 获取香港上市的阿里巴巴股票price
        price_element = self.find(hk_price_locator)
        price = price_element.get_attribute('text')
        assert 200 <= float(price)

    def test_follow_stock_and_get_result(self):
        stock_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "title_container")]/android.widget.TextView[@text="股票"]')
        follow_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "stockCode") and @text="09988"]/../../..//*[contains(@resource-id, "follow_btn")]')
        followed_btn_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "stockCode") and @text="09988"]/../../..//*[contains(@resource-id, "followed_btn")]')

        self.__search('阿里')
        # 点击股票分类
        self.find(stock_btn_locator).click()
        # 点击加自选按钮
        self.find(follow_btn_locator).click()

        # 再次搜索
        self.__search('阿里', False)
        # 点击股票分类
        self.find(stock_btn_locator).click()
        # 获取元素的所有attribute中text
        followed_btn_text = self.find(followed_btn_locator).get_attribute('text')
        assert '已添加' in followed_btn_text

    def test_scroll(self):
        app_size = self.driver.get_window_size()
        TouchAction(self.driver)\
            .long_press(x=app_size['width']/2, y=app_size['height']*0.8)\
            .move_to(x=app_size['width']/2, y=app_size['height']*0.2)\
            .release()\
            .perform()

    def teardown(self):
        # pass
        time.sleep(10)
        self.driver.quit()
