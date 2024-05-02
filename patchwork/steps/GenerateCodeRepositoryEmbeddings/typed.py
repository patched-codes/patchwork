from typing_extensions import TypedDict


class GenerateCodeRepositoryEmbeddingsInputs(TypedDict):
    pass


class GenerateCodeRepositoryEmbeddingsOutputs(TypedDict):
    embedding_name: str
    documents: str
