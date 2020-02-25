from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self, data):
        self.find((By.CSS_SELECTOR, '#corp_name')).send_keys(data['crop_name'])
        self.find((By.CSS_SELECTOR, '#submit_btn')).click()
    
    def get_error_message(self):
        msg = []
        for element in self.find((By.CSS_SELECTOR, '.js_error_msg')):
            msg.append(element.text)
        
        return msg
