import requests
from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWework:

    # APP的
    app_corpsecret = 'cSaCwNGNoRcyErpbII-8SDb1MN23WRfhk5i2BZ_gIPU'
    
    # 客户联系人的
    groupchat_secret = '_hteCZ6Y__Mz-QUd9wmxtrgiFyLMayHJSqsUP_Gx3Wk'

    @classmethod
    def setup_class(cls):

        # groupchat operation
        cls.groupchat = GroupChat()

    def test_get_token(self):
        token = WeWork.get_token(self.app_corpsecret)

        assert token is not None
