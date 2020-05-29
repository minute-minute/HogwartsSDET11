import json
import yaml
import requests
from jsonpath import jsonpath


class BaseApi:
    _params = {}

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

        # 模板内容替换
        # TODO: format实现
        # 将req转为字符串方便替换
        raw:str = yaml.dump(req)
        for k, v in self._params.items():
            # repr 将对象转化为供解释器读取的形式，如符号*
            raw = raw.replace(f"${{{k}}}", repr(v))
        
        req = yaml.safe_load(raw)

        print(req)

        # req_params = req['params']
        # # 通过ininstance可以使取出来的变量含有类型，方便后续使用
        # if isinstance(req_params, dict):
        #     req_params.update()

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

