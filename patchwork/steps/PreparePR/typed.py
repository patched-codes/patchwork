from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __PreparePRRequiredInputs(TypedDict):
    modified_code_files: List["ModifiedCodeFile"]


class PreparePRInputs(__PreparePRRequiredInputs, total=False):
    pr_header: Annotated[str, StepTypeConfig(is_config=True)]
    issue_url: Annotated[str, StepTypeConfig(is_config=True)]


class PreparePROutputs(TypedDict):
    pr_body: str


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
