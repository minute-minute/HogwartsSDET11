import requests
from urllib.parse import urljoin
from test_requests.test_wework.api.wework import WeWork


class CorpTag(WeWork):
    base_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/'
    # groupchat
    secret = '_hteCZ6Y__Mz-QUd9wmxtrgiFyLMayHJSqsUP_Gx3Wk'

    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False

        token = WeWork.get_token(self.secret)
        self.session.params.update({'access_token': token})

        self.api_data = self.api_load('test_requests/test_wework/api/corp_tag.api.yml')

    def get(self, body={}):

        r = self.api_send(self.api_data['get'])
        return r

    # def get(self, body={}):
    #     url = urljoin(self.base_url, 'get_corp_tag_list')
    #     r = self.session.post(url, json=body).json()

    #     return r

    def add(self, body):
        url = urljoin(self.base_url, 'add_corp_tag')
        r = self.session.post(url, json=body).json()

        return r

    def edit(self, body):
        url = urljoin(self.base_url, 'edit_corp_tag')
        r = self.session.post(url, json=body).json()

        return r

    def delete(self, body):
        url = urljoin(self.base_url, 'del_corp_tag')
        r = self.session.post(url, json=body).json()

        return r

