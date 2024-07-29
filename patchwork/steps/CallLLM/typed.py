from pydantic import BaseModel
from typing_extensions import Annotated, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class CallLLMInputs(BaseModel):
    prompt_file: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    prompts: Optional[List[Dict]] = None
    model: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    allow_truncated: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    model_args: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    client_args: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    openai_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    patched_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    google_api_key: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class CallLLMOutputs(BaseModel):
    openai_responses: List[str]
