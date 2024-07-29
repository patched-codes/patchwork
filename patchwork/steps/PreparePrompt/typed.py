from pydantic import BaseModel
from typing_extensions import Annotated, Any, Dict, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class PreparePromptInputs(BaseModel):
    prompt_template_file: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_id: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_value_file: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    prompt_values: Optional[List[Dict[str, Any]]] = None


class PreparePromptOutputs(BaseModel):
    prompts: List[Dict]
