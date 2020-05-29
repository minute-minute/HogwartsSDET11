from appium import webdriver
from appium.webdriver import WebElement
import logging

from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    _driver: webdriver
    _black_list = []
    _error_max = 5
    _error_count = 0

    def __init__(self, driver: webdriver = None):
        self._driver = driver

        logging.basicConfig(level=logging.DEBUG)

    def element_except_handle(func):
        # 装饰器处理获取元素时的异常
        def wrapper(self, *args, **kwargs):
            try:
                logging.info('find element.')

                result = func(*args, **kwargs)
                # 首次调用find方法需要重置
                self._error_count = 0
                return result

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
                        return wrapper(*args, **kwargs)

                logging.error('black list no element, and find element.')
                raise e

        return wrapper

    @element_except_handle
    def find(self, locator, value=None) -> WebElement:
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        return self._driver.find_element(locator, value)

    @element_except_handle
    def find_and_return_text(self, locator, value=None):
        element = self._driver.find_element(*locator) if isinstance(locator, tuple) \
            else self._driver.find_element(locator, value)

        return element.text

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

    # TODO: appium的数据驱动
    def steps(self):
        pass
