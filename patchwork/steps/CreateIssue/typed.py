from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class __CreateIssueRequiredInputs(TypedDict):
    issue_text: str
    issue_title: Annotated[str, IS_CONFIG]
    scm_url: Annotated[str, IS_CONFIG]


class CreateIssueInputs(__CreateIssueRequiredInputs, total=False):
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class CreateIssueOutputs(TypedDict):
    issue_url: str
