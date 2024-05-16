from typing_extensions import NotRequired, TypedDict


class GenerateCodeRepositoryEmbeddingsInputs(TypedDict):
    disable_cache: NotRequired[bool]


class GenerateCodeRepositoryEmbeddingsOutputs(TypedDict):
    embedding_name: str
    documents: str
