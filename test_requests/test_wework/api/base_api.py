import json
from typing import List
import yaml
import requests
from jsonpath import jsonpath


class BaseApi:
    _params = {}
    _result = {}

    def __init__(self):
        pass

    @classmethod
    def format(cls, resp):
        cls.resp = resp

        print(json.dumps(json.loads(resp.text), indent=2, ensure_ascii=False))

    def jsonpath(self, path, resp=None, **kwagrs):
        if resp is None:
            resp = self.resp
        return jsonpath(resp, path)

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

        print('+++++++++++request+++++++++++++')
        print(req)

        # req_params = req['params']
        # # 通过ininstance可以使取出来的变量含有类型，方便后续使用
        # if isinstance(req_params, dict):
        #     req_params.update()

        resp = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )

        self.format(resp)

        return resp.json()

    # 模拟类型httprunner的数据
    def steps_run(self, steps: List[dict]):

        for step in steps:
            # 模板内容替换
            # TODO: format实现
            # 将req转为字符串方便替换
            raw:str = yaml.dump(step)
            for k, v in self._params.items():
                # repr 将对象转化为供解释器读取的形式，如符号*
                raw = raw.replace(f"${{{k}}}", repr(v))
            step = yaml.safe_load(raw)

            if 'method' in  step.keys():
                method = step['method'].split('.')[-1]
                # 获取方法名为method的方法执行
                getattr(self, method)(**step)
            
            if 'extract' in step.keys():
                self._result[step['extract']] = self.jsonpath(**step)
            
            if 'assertion' in step.keys():
                assertion = step['assertion']
                if isinstance(assertion, str):
                    # eval有安全问题，可以借鉴httprunner，封装常用的断言，复杂的使用自定义函数，使用特殊标记（如$()）
                    # TODO: 完善
                    assert eval(assertion)

                if assertion[1] == 'eq':
                    assert assertion[0] == assertion[2]

    @classmethod
    def yaml_load(self, path) -> list:
        with open(path) as f:
            return yaml.safe_load(f)

