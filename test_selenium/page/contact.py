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
        if 'id' in member:
            acctid = (By.NAME, 'acctid')
            self.find(acctid).clear()
            self.find(acctid).send_keys(member['id'])
        if 'name' in member:
            name = (By.NAME, 'username')
            self.find(name).clear()
            self.find(name).send_keys(member['name'])
        if 'gender' in member:
            self.find((By.CSS_SELECTOR, 'input[name="gender"][value="%s"]' % member['gender'])).click()
        if 'mobile_area' in member:
            self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        if 'mobile' in member:
            mobile = (By.NAME, 'mobile')
            self.find(mobile).clear()
            self.find(mobile).send_keys(member['mobile'])
        if 'address' in member:
            address = (By.NAME, 'xcx_corp_address')
            self.find(address).clear()
            self.find(address).send_keys(member['address'])
        if 'title' in member:
            title = (By.NAME, 'position')
            self.find(title).clear()
            self.find(title).send_keys(member['title'])

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
