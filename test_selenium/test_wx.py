import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# import yaml
# project_dir = os.getcwd()
# sys.path.append(project_dir)
# with open(project_dir + r'\test_selenium.yml', 'rb') as f:
#     config = yaml.load(f, Loader=yaml.FullLoader)
config = {
    'debugger_address': '127.0.0.1:9222',
    'test_work_wexin': {
        'cookies': {},
        'wexin_login': 'https://work.weixin.qq.com/wework_admin/frame#index',
        'add_member': [
            {
                'id': 1,
                'name': 'a',
                'gender': '1',
                'mobile': 13511112222,
                'address': '',
                'title': 'test'
            }
        ]
    }
}


class TestWx:
    def setup_class(self):
        options = webdriver.ChromeOptions()
        # close all chrome window, and cmd: chrome.exe --remote-debugging-port=9222
        options.debugger_address = config['debugger_address']
        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def wait_element(self, timeout, method):
        return WebDriverWait(self.driver, timeout=timeout).until(method)

    def element(self, by, value):
        if by == 'css_selector':
            return self.driver.find_element_by_css_selector(value)
        elif by == 'xpath':
            return self.driver.find_element_by_xpath(value)
        else:
            raise BaseException('no such find element method [%s]' % by)

    def login_work_wexin(self):
        work_wexin = config['test_work_wexin']
        cookies = work_wexin['cookies']
        login_url = work_wexin['wexin_login']

        # open work.wexin
        self.driver.get(login_url)

        # cookies = self.driver.get_cookies()
        # {
        #     'domain': cookie['domain'],
        #     'name': cookie['name'],
        #     'value': cookie['value'],
        #     'path': '/',
        #     'expires': None
        # }

        # use cookies login
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

    # @pytest.mark.parametrize('member', config['test_work_wexin']['add_member'])  # 若使用参数化则不用for循环，但每次都需要重新打开一次url和add页面
    def test_work_wexin_add_member(self):
        # login work wexin
        self.login_work_wexin()

        members = config['test_work_wexin']['add_member']

        # add member page
        self.driver.find_element_by_css_selector('[node-type="addmember"]').click()

        # write member info
        last_member_index = len(members) - 1
        for index, member in enumerate(members):
            self.element('css_selector', '#username').send_keys(member['name'])
            self.element('css_selector', '#memberAdd_acctid').send_keys(member['id'])
            self.element('css_selector', 'input[name="gender"][value="%s"]' % member['gender']).click()
            self.element('css_selector', '#memberAdd_phone').send_keys(member['mobile'])
            self.element('css_selector', '#memberEdit_address').send_keys(member['address'])
            self.element('css_selector', '#memberAdd_title').send_keys(member['title'])

            # save member
            if last_member_index != index:
                save = EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"member_colRight_operationBar")]/a[text()="保存并继续添加"]'))
            else:
                save = EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"member_colRight_operationBar")]/a[text()="保存"]'))
            self.wait_element(10, save).click()