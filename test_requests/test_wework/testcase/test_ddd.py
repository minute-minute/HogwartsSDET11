import pytest
from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.corp_tag import CorpTag


class TestCorpTag():
    test_data = BaseApi.yaml_load('test_requests/test_wework/testcase/test_corptag.data.yml')
    test_steps = BaseApi.yaml_load('test_requests/test_wework/testcase/test_corptag.step.yml')

    @classmethod
    def setup_class(cls):
        # TODO： 删除测试数据，将需要数据封装

        cls.corptag = CorpTag()

    @pytest.mark.parametrize('name', test_data['test_add'])
    def test_add_step(self, name):
        self.corptag._params['name'] = name
        self.corptag.steps_run(self.test_steps['test_add'])

    @classmethod
    def teardown_class(cls):
        # teardown清空数据风险比较大，因为一些异常强制退出执行case（如直接kill），会导致走不到teardown
        pass
