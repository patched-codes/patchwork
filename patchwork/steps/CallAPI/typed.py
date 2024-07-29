from pydantic import BaseModel
from typing_extensions import Annotated, Any, Dict, Literal, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class CallAPIInputs(BaseModel):
    url: str
    method: Annotated[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"], StepTypeConfig(is_config=True)]
    headers: Optional[Annotated[Dict[str, str], StepTypeConfig(is_config=True)]] = None
    body: Optional[Dict[str, Any]] = None


class CallAPIOutputs(BaseModel):
    status_code: int
    headers: Dict[str, str]
    body: str
