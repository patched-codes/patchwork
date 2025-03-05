import json
from typing import Any, Dict, Optional

import requests
from typing_extensions import Literal

from patchwork.common.tools.tool import Tool


class APIRequestTool(Tool, tool_name="make_api_request", abc_register=False):
    __base_url = ""
    __headers = dict()
    __auth = None
    __data_prefix = ""

    def __init__(
        self,
        base_url: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        data_prefix: Optional[str] = None,
        **kwargs,
    ):
        if base_url:
            self.__base_url = base_url
        if headers:
            self.__headers = headers
        if username and password:
            self.__auth = (username, password)
        if data_prefix:
            self.__data_prefix = data_prefix

    @property
    def json_schema(self) -> dict:
        return {
            "name": "make_api_request",
            "description": """\
A generic tool to make HTTP API requests with flexible configuration.

Supports various HTTP methods (GET, POST, PUT, DELETE, PATCH) with optional
authentication, headers, query parameters, and request body.

Authentication can be configured via:
- Basic Auth (username/password)
- Bearer Token
- API Key (in header or query param)
""",
            "input_schema": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "Full URL for the API endpoint",
                    },
                    "method": {
                        "type": "string",
                        "enum": ["GET", "POST", "PUT", "DELETE", "PATCH"],
                        "description": "HTTP method for the request",
                    },
                    "headers": {
                        "type": "object",
                        "description": "Optional custom headers",
                    },
                    "params": {
                        "type": "object",
                        "description": "Optional query parameters",
                    },
                    "data": {
                        "type": "string",
                        "description": "data for POST/PUT/PATCH requests. If you need to send json data, it should be converted to a string.",
                    },
                },
                "required": ["url", "method"],
            },
        }

    def execute(
        self,
        url: str,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"] = "GET",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[str] = None,
    ) -> str:
        # Combine with default headers
        request_headers = headers or {}
        request_headers.update(self.__headers)

        # Prepare request
        try:
            response = requests.request(
                method=method,
                url=self.__base_url + url,
                headers=request_headers,
                params=params,
                data=(self.__data_prefix + data if data else None),
                auth=self.__auth,
            )

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Try to parse JSON, fallback to text
            try:
                return json.dumps(response.json(), indent=2)
            except ValueError:
                return response.text
        except requests.RequestException as e:
            if e.response is not None:
                response_text = e.response.text
                status_code = e.response.status_code
                headers = e.response.headers

                header_string = "\n".join(f"{key}: {value}" for key, value in headers.items())

                return (
                    f"HTTP/{e.response.raw.version / 10:.1f} {status_code} {e.response.reason}\n"
                    f"{header_string}\n"
                    f"\n"
                    f"{response_text}"
                )
            else:
                return f"API Request Error: {str(e)}"
