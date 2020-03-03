import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        self.__init_app()

        # 常用元素
        self.__search_locator = (MobileBy.ID, 'tv_search')
        self.__search_input_locator = (MobileBy.ID, 'search_input_text')
        self.__trade_locator = (MobileBy.XPATH, '//*[contains(@resource-id, "tab_name") and @text="交易"]')


    def __init_app(self):
        caps = {}
        caps['deviceName'] = 'xu'
        caps['platformName'] = 'Android'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'

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

    def test_webview_native(self):
        # 不同版本解析出来的页面可能不一样，不太适用

        # 点击交易页
        self.find(self.__trade_locator).click()
        # 点击“A股开户”
        self.find(MobileBy.ACCESSIBILITY_ID, 'A股开户').click()

        # 输入用户名密码登录
        self.find(MobileBy.ACCESSIBILITY_ID, '输入11位手机号').send_keys('13511112222')
        self.find(MobileBy.ACCESSIBILITY_ID, '输入验证码').send_keys('123456')
        self.find(MobileBy.ACCESSIBILITY_ID, '立即开户').click()

    def test_webview_context(self):
        # 切换到webview进行操作

        # 点击交易页
        self.find(self.__trade_locator).click()

        # 切换到webview
        # 注：webview上下文出现大概有3s延迟，
        # android6.0默认支持（mumu模拟器不支持，原生和genymotion支持），其他需要打开webview调试开关
        # 注：chromedriver必须和chrome版本对应
        # 注：chromedriver和chrome若无法对应，须下载对应版本chromedriver版本，
        # 通过capabilities的mapping file映射或直接使用chromedriverExecutable
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])

        # 注：使用chrome://inspect/#devices分析webview界面控件，需要代理、及chrome62及以前的版本
        self.find(By.CSS_SELECTOR, '.trade_home_info_3aI').click()

        # 注：有页面跳转时会出现多个window，需要切换到最上层的进行操作
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)  # 可打印所有window看目前应该处于第几个
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 注：html加载问题，元素存在，但还不可以进行交互，需要显示等待
        phone_locator = (By.ID, 'phone-number')
        WebDriverWait(self, 20).until(expected_conditions.visibility_of_element_located(*phone_locator))
        self.find(phone_locator).send_keys('13511112222')
        self.find(By.ID, 'code').send_keys('123456')
        self.find(By.CSS_SELECTOR, '.btn-submit').click()

    def test_webview_context_2(self):
        # 点击交易页
        self.find(self.__trade_locator).click()

        # 切换到webview
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])

        # 港美股开户
        self.find(By.CSS_SELECTOR, '.trade_home_info_3aI>*[text="港美股开户"]').click()
        # 跳转另一个页面
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 输入手机号与错误的验证码,点击确认
        # 等待页面加载完成
        phone_locator = (By.CSS_SELECTOR, 'input[placeholder="请输入手机号"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone_locator))
        self.find(phone_locator).send_keys('13511112222')
        self.find(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys('1234')
        self.find(By.CSS_SELECTOR, '.open_form-submit_1Ms[text=立即开户]').click()

        # 切换回原生
        self.driver.switch_to.context(self.driver.contexts[0])
        # 点击关闭回到交易页
        self.find(MobileBy.ID, 'action_bar_back').click()

    def teardown(self):
        # pass
        time.sleep(10)
        self.driver.quit()
