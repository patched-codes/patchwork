from typing_extensions import Annotated, Any, Dict, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __CommitChangesRequiredInputs(TypedDict):
    modified_code_files: List[Dict[str, Any]]


class CommitChangesInputs(__CommitChangesRequiredInputs, total=False):
    disable_branch: Annotated[bool, StepTypeConfig(is_config=True)]
    force_branch_creation: Annotated[bool, StepTypeConfig(is_config=True)]
    branch_prefix: Annotated[str, StepTypeConfig(is_config=True)]
    branch_suffix: Annotated[str, StepTypeConfig(is_config=True)]


class CommitChangesOutputs(TypedDict):
    base_branch: str
    target_branch: str
