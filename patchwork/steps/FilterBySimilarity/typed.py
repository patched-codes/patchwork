from typing_extensions import Annotated, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __FilterBySimilarityRequiredInputs(TypedDict):
    list: List[Dict]
    keywords: Annotated[str, StepTypeConfig(is_config=True)]


class FilterBySimilarityInputs(__FilterBySimilarityRequiredInputs, total=False):
    keys: Annotated[str, StepTypeConfig(is_config=True)]
    top_k: Annotated[int, StepTypeConfig(is_config=True)]


class FilterBySimilarityOutputs(TypedDict):
    result_list: List[Dict]
