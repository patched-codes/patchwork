from pydantic import BaseModel
from typing_extensions import Annotated, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class GenerateCodeRepositoryEmbeddingsInputs(BaseModel):
    disable_cache: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None


class GenerateCodeRepositoryEmbeddingsOutputs(BaseModel):
    embedding_name: str
    documents: str
