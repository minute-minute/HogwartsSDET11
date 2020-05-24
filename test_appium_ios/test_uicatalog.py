

from appium import webdriver


class TestUICatalog:
    def setup(self):
        caps = {
            'platformName': 'iOS',
            'platformVersion': '13.4.1',
            'deviceName': 'iPhone 8',
            'automationName': 'XCUITest',
            'udid': 'E180A637-124D-482C-8923-731B7BD3E23C',
            "app": "/Users/minute/Library/Developer/Xcode/DerivedData/UIKitCatalog-dhubypdncuyhndeksoujtcpjfmzh/Build/Products/Debug-iphonesimulator/UIKitCatalog.app", # build完的app路径
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

    def test_button(self):
        self.driver.find_element_by_accessibility_id('Button')

    def teardown(self):
        self.driver.quit()
