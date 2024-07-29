from pydantic import BaseModel
from typing_extensions import Annotated, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class ExtractModelResponseInputs(BaseModel):
    openai_responses: List[str]
    response_partitions: Optional[Annotated[Dict[str, List[str]], StepTypeConfig(is_config=True)]] = None


class ExtractModelResponseOutputs(BaseModel):
    extracted_responses: List[Dict[str, str]]
