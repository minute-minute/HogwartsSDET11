from test_selenium.page.mian import Main


class TestMain:

    def setup_class(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        member = {
            'id': 1,
            'name': 'a',
            'gender': '1',
            'mobile': 13511112222,
            'address': '',
            'title': 'test'
        }
        self.main.add_member().add_member_one(member)
        assert self.main.show_message()

    def test_edit_member(self):
        member_name = '张三（示例）'
        info = {
            'name': 'edit',
            'gender': '1',
            'mobile': 13511112222,
            'address': '',
            'title': 'test'
        }
        self.main.member_info(member_name).add_member_one(info)
        assert self.main.show_message()

    def test_import_user(self):
        self.main.import_user('F:/HogwartsSDET11/test_selenium/testcase/通讯录批量导入模板.xlsx')
        assert self.main.show_message()

    def test_send_message(self):
        message = {
            'app': '公告',
            'group': '许纷纷',
            'content': {
                'title': 'test',
                'body': '1'
            },
            'author': 'test'
        }
        msg = self.main.send_message()
        msg.send(message)
        assert 'test' in msg.get_history()

    def test_upload_image(self):
        self.main.add_material().upload_image('F:/HogwartsSDET11/test_selenium/testcase/test.jpg')
        assert self.main.show_message()
