from __future__ import annotations

from typing_extensions import Annotated, Any, Literal, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CallAPIRequiredInputs(TypedDict):
    url: str
    method: Annotated[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"], IS_CONFIG]


class CallAPIInputs(__CallAPIRequiredInputs, total=False):
    headers: Annotated[dict[str, str], IS_CONFIG]
    body: dict[str, Any]


class CallAPIOutputs(TypedDict):
    status_code: int
    headers: dict[str, str]
    body: str
