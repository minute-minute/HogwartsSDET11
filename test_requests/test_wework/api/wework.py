import requests

from test_requests.test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = 'wwf59ffdcb6d9bef43'

    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    tokens = {}

    def __init__(self):
        pass

    @classmethod
    def get_token(cls, corpsecret):
        if corpsecret not in cls.tokens.keys():
            res = cls.get_access_token(corpsecret)
            cls.tokens[corpsecret] = res['access_token']

        return cls.tokens[corpsecret]

    @classmethod
    def get_access_token(cls, corpsecret):
        res = requests.get(
                cls.token_url, 
                params={
                    'corpid': cls.corpid,
                    'corpsecret': corpsecret
                }, 
                verify=False
                ).json()

        assert res['errcode'] == 0

        return res
