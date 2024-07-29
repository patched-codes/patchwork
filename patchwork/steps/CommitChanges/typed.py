from pydantic import BaseModel
from typing_extensions import Annotated, Any, Dict, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class CommitChangesInputs(BaseModel, total=False):
    modified_code_files: List[Dict[str, Any]]
    disable_branch: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    force_branch_creation: Optional[Annotated[bool, StepTypeConfig(is_config=True)]] = None
    branch_prefix: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None
    branch_suffix: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class CommitChangesOutputs(TypedDict):
    base_branch: str
    target_branch: str
