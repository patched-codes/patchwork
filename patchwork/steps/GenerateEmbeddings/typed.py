from typing_extensions import Any, Iterable, TypedDict


class GenerateEmbeddingsInputs(TypedDict):
    embedding_name: str
    documents: Iterable[dict[str, Any]]
    disable_cache: NotRequired[bool]


class GenerateEmbeddingsOutputs(TypedDict):
    pass
