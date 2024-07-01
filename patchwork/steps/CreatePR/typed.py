from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CreatePRRequiredInputs(TypedDict):
    target_branch: str


class CreatePRInputs(__CreatePRRequiredInputs, total=False):
    base_branch: str
    pr_title: str
    pr_body: str
    force_pr_creation: Annotated[bool, IS_CONFIG]
    disable_pr: Annotated[bool, IS_CONFIG]
    scm_url: Annotated[str, IS_CONFIG]
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class CreatePROutputs(TypedDict):
    pr_url: str
