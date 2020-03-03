from appium import webdriver
from appium.webdriver import WebElement
import logging

from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    _driver: webdriver
    _black_list = [
        (MobileBy.ID, 'tv_agree'),
        (MobileBy.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 5
    _error_count = 0

    def __init__(self, driver: webdriver = None):
        self._driver = driver

        logging.basicConfig(level=logging.DEBUG)

    def find(self, locator, value=None) -> WebElement:
        try:

            element_result = self._driver.find_element(*locator) if isinstance(locator, tuple) \
                else self._driver.find_element(locator, value)
            # 首次调用find方法需要重置
            self._error_count = 0
            return element_result

        except BaseException as e:
            # 退出条件
            if self._error_count > self._error_max:
                raise e

            self._error_count += 1

            for black_locator in self._black_list:
                logging.debug(black_locator)
                elements = self._driver.find_elements(*black_locator)
                if elements:
                    elements[0].click()
                    return self.find(locator, value)

                logging.error('black list no element, and find element.')
                raise e

    # todo: 通过装饰器使每个方法都具有处理异常的能力
    def find_and_get_text(self, locator, value=None) -> WebElement:
        pass

    @staticmethod
    def __text(key):
        return (MobileBy.XPATH, '//*[@text="%s"]' % key)

    @staticmethod
    def __id(key):
        return (MobileBy.ID, key)

    def find_by_text(self, key):
        return self.find(self.__text(key))

    def find_by_id(self, key):
        return self.find(self.__id(key))
