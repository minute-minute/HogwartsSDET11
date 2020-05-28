import json
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
