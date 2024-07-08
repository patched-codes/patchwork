from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.typing import IS_CONFIG


class __ReadIssuesRequiredInputs(TypedDict):
    issue_url: Annotated[str, IS_CONFIG]


class ReadIssuesInputs(__ReadIssuesRequiredInputs, total=False):
    scm_url: Annotated[str, IS_CONFIG]
    gitlab_api_key: Annotated[str, IS_CONFIG]
    github_api_key: Annotated[str, IS_CONFIG]


class ReadIssuesOutputs(TypedDict):
    issue_title: str
    issue_body: str
    issue_comments: list[str]
