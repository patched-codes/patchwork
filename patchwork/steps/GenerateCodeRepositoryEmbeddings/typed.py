from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class GenerateCodeRepositoryEmbeddingsInputs(TypedDict, total=False):
    disable_cache: Annotated[bool, IS_CONFIG]


class GenerateCodeRepositoryEmbeddingsOutputs(TypedDict):
    embedding_name: str
    documents: str
