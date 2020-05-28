from test_requests.test_wework.api.department import Department


class TestDepartment:
    @classmethod
    def setup_class(cls):
        cls.department = Department()

    def test_create_department(self):
        body = {
            "name": "minute研发中心",
            "name_en": "M", # not required
            "parentid": 1,
            "order": 2, # not required
            # "id": 3 # not required
        }
        r = self.department.create(body)

        print(r)

        assert r['errcode'] == 0

    def test_update_department(self):
        body = {
            "id": 4,
            # "name": "minute", # not required
            "name_en": "MI", # not required
            # "parentid": 1, # not required
            # "order": 2 # not required
        }
        r = self.department.update(body)

        print(r)

        assert r['errcode'] == 0

    def test_get_department(self):
        department_id = 1
        r = self.department.get(department_id)

        print(r)

        assert r['errcode'] == 0
        assert len(r['department']) == 4
        
        has_department = self.department.jsonpath(r, '$.department[?(@.name == "minute研发中心")]')
        assert has_department

    def test_delete_department(self):
        department_id = 4
        r = self.department.delete(department_id)

        print(r)

        assert r['errcode'] == 0

    @classmethod
    def teardown_class(cls):
        pass
