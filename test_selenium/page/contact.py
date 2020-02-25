# 1.以业务功能分类
# 2.不要暴露详细操作细节
# 3.断言在case中
# 4.方法应该返回其他的PO或者用于断言的数据
# 5.用到才写成PO，不需要全量写出来

# pyPOM、selenium-python(page object)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage

class Contact(BasePage):

    def __click_save_btn(self):
        # add member page
        save = EC.element_to_be_clickable(
            (By.XPATH, '//div[contains(@class,"member_colRight_operationBar")]/a[text()="保存"]'))
        self.wait_element(10, save).click()

    def __input_member_data(self, member):
        # write member info
        self.find((By.NAME, 'acctid')).send_keys(member['id'])
        self.find((By.NAME, 'username')).send_keys(member['name'])
        self.find((By.CSS_SELECTOR, 'input[name="gender"][value="%s"]' % member['gender'])).click()
        self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find((By.NAME, 'mobile')).send_keys(member['mobile'])
        self.find((By.NAME, 'xcx_corp_address')).send_keys(member['address'])
        self.find((By.NAME, 'position')).send_keys(member['title'])

    def add_member_more(self, member):
        self.__input_member_data(member)
        # save member
        save = EC.element_to_be_clickable(
            (By.XPATH, '//div[contains(@class,"member_colRight_operationBar")]/a[text()="保存并继续添加"]'))
        self.wait_element(10, save).click()

    def add_member_one(self, member):
        self.__input_member_data(member)

        # save member
        self.__click_save_btn()

    def add_member_fail(self, data):
        self.__click_save_btn()

    def search(self, name):
        pass

    def import_member(self, data):
        pass

    def export_member(self):
        pass

    def set_department(self):
        pass

    def delete(self, data):
        pass
