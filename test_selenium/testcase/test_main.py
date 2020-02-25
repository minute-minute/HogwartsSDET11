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
    
    def test_import_user(self):
        self.main.import_user("xxx.file")
        assert self.mian.show_message()
    
    def test_send_message(self):
        message = {}
        self.main.send_message(message)
        assert self.mian.show_message()
