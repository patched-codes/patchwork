from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CreateIssueCommentRequiredInputs(TypedDict):
    issue_text: str
    issue_url: Annotated[str, IS_CONFIG]


class CreateIssueCommentInputs(__CreateIssueCommentRequiredInputs, total=False):
    scm_url: Annotated[str, IS_CONFIG]
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class CreateIssueCommentOutputs(TypedDict):
    issue_comment_url: str
