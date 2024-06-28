from __future__ import annotations

from typing_extensions import TypedDict, Any, Literal


class CallAPIInputs(TypedDict):
    url: str
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"]
    headers: dict[str, str]
    body: dict[str, Any]
    is_fail_on_3xx: bool
    is_fail_on_4xx: bool
    is_fail_on_5xx: bool


class CallAPIOutputs(TypedDict):
    status_code: int
    headers: dict[str, str]
    body: str
