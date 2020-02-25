import time

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Message(BasePage):
    def send(self, message):
        # 选择应用
        self.find(By.CSS_SELECTOR, '.js_select_apps_btn').click()
        self.find(By.CSS_SELECTOR, 'div[data-name="%s"]' % message['app']).click()
        self.find(By.LINK_TEXT, '确定').click()

        # 选择发送范围
        self.find(By.CSS_SELECTOR, '.js_select_range_btn').click()
        self.finds(By.CSS_SELECTOR, '.ww_searchInput_text')[-1].send_keys(message['group'])
        self.find(By.CSS_SELECTOR, '#searchResult li').click()
        self.find(By.LINK_TEXT, '确认').click()

        # 发送内容
        self.find(By.CSS_SELECTOR, 'input[class~="ww_editorTitle"]').send_keys(message['content']['title'])
        # iframe
        iframe = self.find(By.TAG_NAME, 'iframe')
        self._driver.switch_to.frame(iframe)
        self.find(By.TAG_NAME, 'body').send_keys(message['content']['body'])
        self._driver.switch_to.parent_frame()
        # 切换到主页面
        # self._driver.switch_to.default_content()
        self.find(By.CLASS_NAME, 'js_amrd_sendName').send_keys(message['author'])
        # 发送
        self.finds(By.CLASS_NAME, 'js_save_send')[-1].click()
        self.find(By.LINK_TEXT, '确定').click()

    def get_history(self):
        # self.find(By.LINK_TEXT, '已发送').click()
        history_message_element = self.finds(By.CLASS_NAME, 'msg_history_msgList_td')

        history_message = list()
        for e in history_message_element:
            history_message.append(e.text)

        return history_message
