import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestSelenium:

    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome()
        # 隐式等待, 获取element的超时时间
        self.driver.implicitly_wait(5)
    
    @classmethod
    def teardown_class(self):
        self.driver.quit()

    def test_testerhome(self):
        self.driver.get('https://testerhome.com')

        teams = self.driver.find_element_by_link_text('社团')
        teams.click()

        # 显式等待, 实现WebDriverWait
        # poll_frequency 指定报错，未知原因
        # hogwarts = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, '霍格沃兹测试学院')))

        # 立刻获取该指定element
        # hogwarts = self.driver.find_element_by_link_text('霍格沃兹测试学院')

        # css selector会等待页面渲染完成
        hogwarts = self.driver.find_element_by_css_selector('[data-name="霍格沃兹测试学院"]')
        hogwarts.click()

        # topics = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//a[contains(@href, "/topics")]')
        topics = self.driver.find_elements_by_css_selector('div[class="panel-body"] a[href^="/topics"]')
        topics[0].click()

        user = self.driver.find_element_by_css_selector('#user_login')

        user.send_keys('12333hska')

        time.sleep(5)

    def test_2(self):
        self.driver.get('https://testerhome.com')

        topic_element = self.driver.find_element_by_css_selector('a[title="MTSC2020 中国互联网测试开发大会议题征集"]')
        topic_element.click()

        dir_btn_element = self.driver.find_element_by_css_selector('.toc-container button')
        dir_btn_element.click()

        # element = self.driver.find_element_by_css_selector('.toc-container .toc-panel ul li')[3]
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//li[contains(@class,"toc-item")]/a[text()="征集议题范围"]')
        element.click()

        time.sleep(5)


    def test_3(self):
        # performance性能指标
        self.driver.execute_script('return JSON.stringify(performance.timeling);')

        

    
