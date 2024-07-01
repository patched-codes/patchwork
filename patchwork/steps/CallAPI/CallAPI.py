import json

from requests import request

from patchwork.step import Step


class CallAPI(Step):
    def __init__(self, inputs):
        self.url = inputs["url"]
        self.method = inputs["method"]
        possible_headers = inputs.get("headers", {})
        if not isinstance(possible_headers, dict):
            possible_headers = json.loads(possible_headers)
        self.headers = possible_headers
        self.body = inputs.get("body")
        if self.body and isinstance(self.body, dict):
            self.body = json.dumps(self.body)

    def run(self):
        res = request(self.method, self.url, headers=self.headers, data=self.body)
        return dict(status_code=res.status_code, headers=res.headers, body=res.text)
