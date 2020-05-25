import json
from jsonpath import jsonpath
from jsonschema import validate
import requests
from requests import *

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'https://127.0.0.1:8888'
}


def test_requests():
    res = requests.get('https://home.testing-studio.com/categories')
    print(res.status_code)
    status = res.status_code
    assert status == 200


def test_get():
    param = {
        'a': 1, 
        'b': 2, 
        'c': 3
    }
    res = requests.get('https://httpbin.testing-studio.com/get', params=param, proxies=proxies, verify=False)
    print(res.json())
    assert res.status_code == 200


def test_post():
    param = {
        'a': 1, 
        'b': 2, 
        'c': 3
    }
    header = {
        'test': 'demo'
    }
    res = requests.post('https://httpbin.testing-studio.com/post', data=param, headers=header, proxies=proxies, verify=False)
    print(res.json())
    assert res.status_code == 200


def test_upload():
    header = {
        'Content-Type': ''
    }

    res = requests.post('https://httpbin.testing-studio.com/post', 
                        files={'file': open('/Users/minute/develop/project/HogwartsSDET11/test_requests/file.py', 'rb')}, 
                        headers=header,
                        cookies={'name': 'minute'},
                        proxies=proxies, 
                        verify=False
                        )
    print(res.json())
    assert res.status_code == 200



def test_session():
    s = Session()
    s.proxies = proxies
    s.verify = False
    s.headers.update({'name': 'minute'})

    param = {
        'a': 1, 
        'b': 2, 
        'c': 3
    }
    res = s.get('https://httpbin.testing-studio.com/get', params=param, headers={'x-test': '1'})
    print(res.json())
    assert res.status_code == 200


def test_get_hook():
    # TODO: r的用法
    def modify_response(r: Response, *args, **kwargs):
        # r.content = 'ok hook success'
        r.demo = 'demo name'
        return r

    param = {
        'a': 1, 
        'b': 2, 
        'c': 3
    }
    res = requests.get('https://httpbin.testing-studio.com/get', 
                        params=param, 
                        proxies=proxies, 
                        verify=False, 
                        hooks={'response': [modify_response]}
                        )
    print(res.json())
    assert res.status_code == 200

def test_jsonpath():
    res = requests.get('https://home.testing-studio.com/categories.json')
    assert res.status_code == 200

    # r = json.dumps(res.json(), indent=2, ensure_ascii=False)
    r = jsonpath(res.json(), '$..categories[?(@.name=="开源项目")]')
    print(r)

    description = r[0]['description']
    assert description == "开源项目交流与维护"

def test_schema():
    res = requests.get('https://home.testing-studio.com/categories.json')
    assert res.status_code == 200

    r = json.dumps(res.json(), indent=2, ensure_ascii=False)
    print(r)

    # TODO: 待生成文件
    with open('categories_schema.json') as f:
        schema = json.loads(f)
        validate(r.json, schema)
