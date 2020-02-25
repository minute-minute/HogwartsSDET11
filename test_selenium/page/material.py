from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Material(BasePage):

    def upload_image(self, image):
        self.find(By.CSS_SELECTOR, 'a[href*="image"]').click()
        self.find(By.PARTIAL_LINK_TEXT, '添加图片').click()
        self.find(By.CSS_SELECTOR, '#js_upload_input').send_keys(image)

        # 文件上传需要时间，未上传完成点击无效
        display = 0
        while display < 100:
            displayed = self.find(By.CSS_SELECTOR, '#image-gallery320').is_displayed()
            if displayed:
                break
            display += 1
        self.find(By.CSS_SELECTOR, 'a[d_ck="submit"]').click()

