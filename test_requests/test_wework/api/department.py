import requests
from test_requests.test_wework.api.wework import WeWork
from urllib.parse import urljoin


class Department(WeWork):
    base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/'
    # sync_of_contacts
    secret = 'xdFfp4IPDSljjc6W6Gx9hZgriN1PEb_hUh-mW6ZzhDE'

    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False

        token = WeWork.get_token(self.secret)
        self.session.params.update({'access_token': token})

    def create(self, body):
        url = urljoin(self.base_url, 'create')
        r = self.session.post(url, json=body).json()

        return r

    def update(self, body):
        url = urljoin(self.base_url, 'update')
        r = self.session.post(url, json=body).json()

        return r

    def delete(self, department_id):
        url = urljoin(self.base_url, 'delete')
        self.session.params.update({'id': department_id})
        r = self.session.get(url).json()

        return r

    def get(self, department_id):
        url = urljoin(self.base_url, 'list')
        self.session.params.update({'id': department_id})
        r = self.session.get(url).json()

        return r
