from appium import webdriver
from appium.webdriver import WebElement


class BasePage:

    def __init__(self, driver: webdriver = None):
        self._driver = driver

    # todo: 评价、广告等弹窗需要进行异常处理，会阻碍正常逻辑
    def find(self, by, value=None) -> WebElement:
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        return self._driver.find_element(by, value)
