import requests
from urllib.parse import urljoin
from test_requests.test_wework.api.wework import WeWork
from test_requests.test_wework.api.base_api import BaseApi


def api(func):
    def magic(*args, **kwargs):
        base_api: BaseApi = args[0]

        base_api._params = kwargs

        method = func.__name__
        req = base_api.api_load('test_requests/test_wework/api/corp_tag.api.yml')[method]

        return base_api.api_send(req)

        # func(*args, **kwargs)

    return magic


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

    def get(self, body={}, **kwargs):
        '''步骤驱动'''

        r = self.api_send(self.api_data['get'])

        return r

    # def get(self, body={}):
        '''原始方法，通过测试case传入'''
    #     url = urljoin(self.base_url, 'get_corp_tag_list')
    #     r = self.session.post(url, json=body).json()

    #     return r

    def add(self, name, **kwargs):
        '''步骤驱动'''
        # TODO: 装饰器解决参数替换

        self._params['name'] = name

        r = self.api_send(self.api_data['add'])

        return r

    # def add(self, body):
    #     url = urljoin(self.base_url, 'add_corp_tag')
    #     r = self.session.post(url, json=body).json()

    #     return r

    def edit(self, body):
        url = urljoin(self.base_url, 'edit_corp_tag')
        r = self.session.post(url, json=body).json()

        return r

    # def delete(self, body):
    #     url = urljoin(self.base_url, 'del_corp_tag')
    #     r = self.session.post(url, json=body).json()

    #     return r

    def delete(self, tag_id=[], group_id=[]):
        '''步骤驱动'''
        # TODO: 装饰器解决参数替换

        self._params['tag_id'] = tag_id
        self._params['group_id'] = group_id

        r = self.api_send(self.api_data['delete'])
        return r

    @api
    def decorator(self, test):
        pass
