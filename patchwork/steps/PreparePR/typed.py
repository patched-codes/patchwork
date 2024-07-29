from pydantic import BaseModel
from typing_extensions import Annotated, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class PreparePRInputs(BaseModel):
    modified_code_files: List["ModifiedCodeFile"]
    pr_header: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class PreparePROutputs(BaseModel):
    pr_body: str


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
