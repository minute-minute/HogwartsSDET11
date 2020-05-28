from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.corp_tag import CorpTag


class TestCorpTag():
    @classmethod
    def setup_class(cls):
        # TODO： 删除测试数据，将需要数据封装

        cls.corptag = CorpTag()

    def test_get_corp_tag(self):
        body = {
            "tag_id": [
                "etXXXXXXXXXX",
                "etYYYYYYYYYY"
            ]
        }
        r = self.corptag.get()

        print(r)

        assert r['errcode'] == 0

    def test_add_corp_tag(self):
        # tag.name required
        body = {
            "group_id": "eta5cUCgAARJtCoUzDTc2CtbCc_avCXQ",
            # "group_name": "GROUP_NAME",
            # "order": 1,
            "tag": [{
                    "name": "TAG_NAME_1",
                    # "order": 1
                },
                # {
                #     "name": "TAG_NAME_2",
                #     "order": 2
                # }
            ]
        }
        r = self.corptag.add(body)

        print(r)

        assert r['errcode'] == 0

    def test_edit_corp_tag(self):
        # tag.name required
        body = {
            "id": "eta5cUCgAAYVSsXdp5uFvbbim6ktAzhQ", # required
            "name": "NEW_TAG_NAME",
            "order": 1
        }
        r = self.corptag.edit(body)

        print(r)

        assert r['errcode'] == 0

    def test_delete_corp_tag(self):
        name = "TAG_NAME_1"
        tags_path = '$..tag[?(@.name != "")]'
        find_tag_path = '$..tag[?(@.name=="{}")]'.format(name)

        print(find_tag_path)

        add_body = {
            "group_id": "eta5cUCgAARJtCoUzDTc2CtbCc_avCXQ",
            "tag": [{
                    "name": name
                }
            ]
        }
        # 获取原始数据
        source_tags = self.corptag.get()

        # 删除测试标签
        exist_name = self.corptag.jsonpath(source_tags, find_tag_path)
        if exist_name:
            self.corptag.delete({
                "tag_id": [
                    exist_name[0]['id']
                ]
            })

        # 环境清理后开始测试
        source_tags = self.corptag.get()
        source_tags_size = len(self.corptag.jsonpath(source_tags, tags_path))
        print(source_tags_size)

        # 添加tag
        self.corptag.add(add_body)
        add_tags = self.corptag.get()
        print(add_tags)
        assert len(self.corptag.jsonpath(add_tags, tags_path)) == (source_tags_size + 1)

        # 取得添加tag的id
        result = self.corptag.jsonpath(add_tags, find_tag_path)
        print(result)

        # 删除tag
        delete_body = {
            "tag_id": [
                result[0]['id']
            ]
        }
        r = self.corptag.delete(delete_body)

        # 断言
        print(r)
        assert r['errcode'] == 0

    @classmethod
    def teardown_class(cls):
        # teardown清空数据风险比较大，因为一些异常强制退出执行case（如直接kill），会导致走不到teardown
        pass
