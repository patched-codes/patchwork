import json
from typing import Any, Callable, Dict, Optional

import requests
from typing_extensions import Literal

from patchwork.common.tools.tool import Tool
from patchwork.logger import logger


class APIRequestTool(Tool, tool_name="make_api_request", abc_register=False):
    def __init__(
        self,
        headers: Optional[Dict[str, str]] = dict(),
        username: Optional[str] = None,
        password: Optional[str] = None,
        preprocess_data: Callable[[str], str] = lambda x: x,
        **kwargs,
    ):
        self._headers = headers
        self._auth = (username, password) if username and password else None
        self._preprocess_data = preprocess_data

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
        request_headers.update(self._headers)

        # Prepare request
        response = requests.request(
            method=method,
            url=url,
            headers=request_headers,
            params=params,
            data=(self._preprocess_data(data) if data else None),
            auth=self._auth,
        )

        if not response.ok:
            response_text = response.text
            status_code = response.status_code
            headers = response.headers

            header_string = "\n".join(f"{key}: {value}" for key, value in headers.items())

            msg = (
                f"HTTP/{response.raw.version / 10:.1f} {status_code} {response.reason}\n"
                f"{header_string}\n"
                f"\n"
                f"{response_text}"
            )

            logger.debug(msg)

            return (
                f"HTTP/{response.raw.version / 10:.1f} {status_code} {response.reason}\n"
                f"{header_string}\n"
                f"\n"
                f"{response_text}"
            )

        # Try to parse JSON, fallback to text
        try:
            return json.dumps(response.json())
        except ValueError:
            return response.text
