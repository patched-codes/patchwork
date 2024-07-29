from pydantic import BaseModel
from typing_extensions import Annotated, Any, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class GenerateEmbeddingsInputs(BaseModel):
    embedding_name: Annotated[str, StepTypeConfig(is_config=True)]
    documents: List[Dict[str, Any]]
    disable_cache: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None


class GenerateEmbeddingsOutputs(BaseModel):
    pass
