from typing_extensions import Annotated, Any, Dict, Literal, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CallAPIRequiredInputs(TypedDict):
    url: str
    method: Annotated[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"], StepTypeConfig(is_config=True)]


class CallAPIInputs(__CallAPIRequiredInputs, total=False):
    headers: Annotated[Dict[str, str], StepTypeConfig(is_config=True)]
    body: Dict[str, Any]


class CallAPIOutputs(TypedDict):
    status_code: int
    headers: Dict[str, str]
    body: str
