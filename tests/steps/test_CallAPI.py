import json

import pytest

from patchwork.steps.CallAPI.CallAPI import (
    CallAPI,
)


@pytest.mark.parametrize(
    "method, path, headers, body, return_code",
    [
        ["GET", "/", None, None, 200],
        ["POST", "/", None, None, 200],
        ["POST", "/", None, None, 404],
        ["POST", "/something", None, None, 200],
        ["POST", "/something", {"header1": "value"}, None, 200],
        ["POST", "/something", '{"header1": "value"}', None, 200],
        ["POST", "/something", {"Content-Type": "text/plain"}, "something", 200],
        ["POST", "/something", {"Content-Type": "text/plain"}, {"key": "value"}, 200],
        ["POST", "/something", {"Content-Type": "text/plain"}, '{"key": "value"}', 200],
    ],
)
def test_call_api_outputs(httpserver, path, method, headers, body, return_code):
    response_body = "some data"
    response_headers = {"Content-Type": "text/plain"}
    httpserver.serve_content(content=response_body, headers=response_headers, code=return_code)

    inputs = {"url": f"{httpserver.url}{path}", "method": method}
    if headers:
        inputs["headers"] = headers
    if body:
        inputs["body"] = body

    expected_headers = None
    if headers is not None:
        expected_headers = headers if isinstance(headers, dict) else json.loads(headers)

    result = CallAPI(inputs).run()

    request = httpserver.requests[-1]
    assert request.method == method
    assert request.path == path
    if expected_headers is not None:
        for key, value in expected_headers.items():
            assert request.headers[key] == value

    assert result["status_code"] == return_code
    assert result["body"] == response_body
    assert result["headers"]["Content-Type"] == response_headers["Content-Type"]
