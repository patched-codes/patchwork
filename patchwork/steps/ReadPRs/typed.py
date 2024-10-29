from typing_extensions import Annotated, List, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.ReadPRDiffs.typed import ReadPRDiffsOutputs


class __ReadPRsRequiredInputs(TypedDict):
    repo_slug: str


class ReadPRsInputs(__ReadPRsRequiredInputs, total=False):
    pr_state: str
    scm_url: Annotated[str, StepTypeConfig(is_config=True)]
    gitlab_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["github_api_key"])]
    github_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["gitlab_api_key"])]


class ReadPRsOutputs(TypedDict):
    pr_texts: List[ReadPRDiffsOutputs]
