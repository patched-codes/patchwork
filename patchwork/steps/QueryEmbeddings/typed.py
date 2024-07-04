from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __QueryEmbeddingsRequiredInputs(TypedDict):
    embedding_name: str
    texts: list[str]


class QueryEmbeddingsInputs(__QueryEmbeddingsRequiredInputs, total=False):
    top_k: Annotated[int, IS_CONFIG]
    token_limit: Annotated[int, IS_CONFIG]


class QueryEmbeddingsOutputs(TypedDict):
    embedding_results: list[dict[str, Any]]
