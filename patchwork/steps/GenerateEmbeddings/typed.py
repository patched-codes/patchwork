from typing import Any

from typing_extensions import Iterable, TypedDict, NotRequired


class GenerateEmbeddingsInputs(TypedDict):
    embedding_name: str
    documents: Iterable[dict[str, Any]]
    disable_cache: NotRequired[bool]


class GenerateEmbeddingsOutputs(TypedDict):
    pass
