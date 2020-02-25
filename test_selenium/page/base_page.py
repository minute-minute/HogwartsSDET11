import time
from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    _base_url = ''

    def __init__(self, driver: WebDriver=None, reuse=False):
        debugger_address = '127.0.0.1:9222'

        if driver is None:
            options = webdriver.ChromeOptions()
            # 复用原有浏览器
            if reuse:
                # close all chrome window, and cmd: chrome.exe --remote-debugging-port=9222
                options.debugger_address = debugger_address

            self._driver = webdriver.Chrome(options=options)

            self._driver.implicitly_wait(3)

            if self._base_url != '':
                self._driver.get(self._base_url)

        else:
            self._driver = driver

    def wait_element(self, timeout, method):
        return WebDriverWait(self._driver, timeout=timeout).until(method)

    def find(self, by, locator="") -> WebElement:
        if isinstance(by, tuple):
            return self._driver.find_element(*by)

        print(locator)

        return self._driver.find_element(by, locator)

    def finds(self, by, locator="") -> List[WebElement]:
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)

        print(locator)

        return self._driver.find_elements(by, locator)

    def close(self):
        time.sleep(10)
        self._driver.quit()
