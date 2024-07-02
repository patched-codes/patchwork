from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CreatePRCommentRequiredInputs(TypedDict):
    pr_url: str
    pr_comments: str


class CreatePRCommentInputs(__CreatePRCommentRequiredInputs, total=False):
    noisy_comments: Annotated[bool, IS_CONFIG]
    scm_url: Annotated[str, IS_CONFIG]
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class CreatePRCommentOutputs(TypedDict):
    pass
