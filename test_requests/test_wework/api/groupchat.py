
import requests
from urllib.parse import urljoin
from test_requests.test_wework.api.wework import WeWork


class GroupChat:
    # TODO: 自动加解密
    # TODO: 多环境支持，根据配置可以一套case测试多套环境，需要修改host

    base_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/'
    # 客户联系人的
    groupchat_secret = '_hteCZ6Y__Mz-QUd9wmxtrgiFyLMayHJSqsUP_Gx3Wk'

    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'https://127.0.0.1:8888'
    }

    def __init__(self):
        # 建立一个会话，复用
        self.groupchat_session = requests.Session()
        self.groupchat_session.proxies = self.proxies
        self.groupchat_session.verify = False

        # token
        self.groupchat_session.params['access_token'] = WeWork.get_token(self.groupchat_secret)

    def list(self, body={}):
        url = urljoin(self.base_url, 'list')
        
        default_body = {
            "offset": 0,
            "limit": 100
        }
        body = {**default_body, **body}

        r = self.groupchat_session.post(url, json=body)

        res = r.json()

        return res

    def get(self, chat_id):
        url = url = urljoin(self.base_url, 'get')
        body = {
            "chat_id": chat_id
        }

        r = self.groupchat_session.post(url, json=body)

        res = r.json()

        return res
