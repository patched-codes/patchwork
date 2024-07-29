from typing_extensions import Annotated, List, Optional, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig

class __ReadPRDiffsRequiredInputs(TypedDict):
    pr_url: str

class ReadPRDiffsInputs(__ReadPRDiffsRequiredInputs, total=False):
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True)]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True)]


class ReadPRDiffsOutputs(TypedDict):
    prompt_values: List["Diff"]


class Diff(TypedDict):
    path: str
    diff: str
