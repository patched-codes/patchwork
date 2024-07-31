from typing_extensions import Annotated, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class GenerateCodeRepositoryEmbeddingsInputs(TypedDict, total=False):
    disable_cache: Annotated[bool, StepTypeConfig(is_config=True)]


class GenerateCodeRepositoryEmbeddingsOutputs(TypedDict):
    embedding_name: str
    documents: str
