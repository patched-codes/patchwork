from __future__ import annotations

from typing_extensions import Any, Literal, TypedDict


class __CallAPIRequiredInputs(TypedDict):
    url: str
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"]


class CallAPIInputs(__CallAPIRequiredInputs, total=False):
    headers: dict[str, str]
    body: dict[str, Any]


class CallAPIOutputs(TypedDict):
    status_code: int
    headers: dict[str, str]
    body: str
