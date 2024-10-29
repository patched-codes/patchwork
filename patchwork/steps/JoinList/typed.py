from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __JoinListRequiredInputs(TypedDict):
    list: List[Dict]
    delimiter: Annotated[str, StepTypeConfig(is_config=True)]


class JoinListInputs(__JoinListRequiredInputs, total=False):
    key: str


class JoinListOutputs(TypedDict):
    text: str
