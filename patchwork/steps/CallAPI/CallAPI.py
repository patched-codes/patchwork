from patchwork.step import Step
from requests import request


class CallAPI(Step):
    def __init__(self, inputs):
        self.url = inputs["url"]
        self.method = inputs["method"]
        self.headers = inputs.get("headers", "{}")
        self.body = inputs.get("body")
        self.is_fail_on_3xx = inputs.get("is_fail_on_3xx", False)
        self.is_fail_on_4xx = inputs.get("is_fail_on_4xx", False)
        self.is_fail_on_5xx = inputs.get("is_fail_on_5xx", False)

    def run(self):
        res = request(self.method, self.url, headers=self.headers, data=self.body)
        status_code = res.status_code
        if (
                (self.is_fail_on_3xx and 300 <= status_code < 400) or
                (self.is_fail_on_4xx and 400 <= status_code < 500) or
                (self.is_fail_on_5xx and 500 <= status_code < 600)
        ):
            raise ValueError(f"Request failed with status code {status_code}")

        return dict(
            status_code=res.status_code,
            headers=res.headers,
            body=res.text
        )
