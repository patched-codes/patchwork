from __future__ import annotations
from typing_extensions import Any, NotRequired, TypedDict


class QueryEmbeddingsInputs(TypedDict):
    embedding_name: str
    texts: list[str]
    top_k: NotRequired[int]
    token_limit: NotRequired[int]


class QueryEmbeddingsOutputs(TypedDict):
    embedding_results: list[dict[str, Any]]
