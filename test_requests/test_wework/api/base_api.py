import json
import yaml
import requests
from jsonpath import jsonpath


class BaseApi:
    def __init__(self):
        pass

    @classmethod
    def format(cls, r):
        cls.r = r

        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    def jsonpath(self, r, path):
        return jsonpath(r, path)

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, req: dict):
        req['params']['access_token'] = self.get_token(self.secret)


        r = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        return r.json()

    @classmethod
    def yaml_load(self, path) -> list:
        with open(path) as f:
            return yaml.safe_load(f)

