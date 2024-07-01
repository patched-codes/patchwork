from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __GenerateEmbeddingsRequiredInputs(TypedDict):
    embedding_name: Annotated[str, IS_CONFIG]
    documents: list[dict[str, Any]]


class GenerateEmbeddingsInputs(__GenerateEmbeddingsRequiredInputs, total=False):
    disable_cache: Annotated[bool, IS_CONFIG]


class GenerateEmbeddingsOutputs(TypedDict):
    pass
