from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __QueryEmbeddingsRequiredInputs(TypedDict):
    embedding_name: str
    texts: List[str]


class QueryEmbeddingsInputs(__QueryEmbeddingsRequiredInputs, total=False):
    top_k: Annotated[int, StepTypeConfig(is_config=True)]
    token_limit: Annotated[int, StepTypeConfig(is_config=True)]


class QueryEmbeddingsOutputs(TypedDict):
    embedding_results: List[Dict[str, Any]]
