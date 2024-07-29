from pydantic import BaseModel
from typing_extensions import Annotated, Iterable, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class CallCode2PromptInputs(BaseModel):
    folder_path: Annotated[str, StepTypeConfig(is_config=True, is_path=True)]
    filter: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    suppress_comments: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None


class CallCode2PromptOutputs(BaseModel):
    files_to_patch: Iterable[dict]
