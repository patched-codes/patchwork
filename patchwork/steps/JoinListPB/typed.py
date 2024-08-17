from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class JoinListPBInputs(TypedDict):
    key: str
    list: List[Dict]
    delimiter: Annotated[str, StepTypeConfig(is_config=True)]


class JoinListPBOutputs(TypedDict):
    text: str
