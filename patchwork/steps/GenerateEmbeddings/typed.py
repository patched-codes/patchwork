from typing_extensions import Annotated, Any, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig

class __GenerateEmbeddingsRequiredInputs(TypedDict):
    embedding_name: Annotated[str, StepTypeConfig(is_config=True)]
    documents: List[Dict[str, Any]]

class GenerateEmbeddingsInputs(__GenerateEmbeddingsRequiredInputs, total=False):
    disable_cache: Annotated[bool, StepTypeConfig(is_config=True)]


class GenerateEmbeddingsOutputs(TypedDict):
    pass
