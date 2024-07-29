from pydantic import BaseModel
from typing_extensions import Annotated, List

from patchwork.common.utils.step_typing import StepTypeConfig


class JoinListInputs(BaseModel):
    list: List[str]
    delimiter: Annotated[str, StepTypeConfig(is_config=True)]


class JoinListOutputs(BaseModel):
    text: str
