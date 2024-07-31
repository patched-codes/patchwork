from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __ExtractModelResponseRequiredInputs(TypedDict):
    openai_responses: List[str]


class ExtractModelResponseInputs(__ExtractModelResponseRequiredInputs, total=False):
    response_partitions: Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]


class ExtractModelResponseOutputs(TypedDict):
    extracted_responses: List[Dict[str, str]]
