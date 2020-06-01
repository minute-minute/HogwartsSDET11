import pytest
from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.corp_tag import CorpTag


class TestDDD():
    test_data = BaseApi.yaml_load('test_requests/test_wework/testcase/test_corptag.all.yml')

    @classmethod
    def setup_class(cls):
        cls.corptag = CorpTag()

        # 清除数据
        cls.corptag.get()
        for name in cls.test_data['test_add']['data']:
            x = cls.corptag.jsonpath("$..tag[?(@.name=='{}')]".format(name))
            if x:
                cls.corptag.delete(tag_id=[x[0]['id']])

    @pytest.mark.parametrize('name', test_data['test_add']['data'])
    def test_add_step(self, name):
        self.corptag._params['name'] = name
        self.corptag.steps_run(self.test_data['test_add']['steps'])

    @classmethod
    def teardown_class(cls):
        pass
