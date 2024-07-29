from typing_extensions import Annotated, List

from patchwork.common.utils.step_typing import StepTypeConfig


class JoinListInputs(TypedDict):
    list: List[str]
    delimiter: Annotated[str, StepTypeConfig(is_config=True)]


class JoinListOutputs(TypedDict):
    text: str
