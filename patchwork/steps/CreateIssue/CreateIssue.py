from pathlib import Path

import git

from patchwork.common.client.scm import (
    GithubClient,
    GitlabClient,
    ScmPlatformClientProtocol,
    get_slug_from_remote_url,
)
from patchwork.logger import logger
from patchwork.step import Step


class CreateIssue(Step):
    required_keys = {"issue_title", "issue_text", "scm_url"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.scm_client: ScmPlatformClientProtocol
        if "github_api_key" in inputs.keys():
            self.scm_client = GithubClient(inputs["github_api_key"])
        elif "gitlab_api_key" in inputs.keys():
            self.scm_client = GitlabClient(inputs["gitlab_api_key"])
        else:
            raise ValueError(f'Missing required input data: "github_api_key" or "gitlab_api_key"')

        self.scm_client.set_url(inputs["scm_url"])

        self.issue_title = inputs["issue_title"]
        self.issue_text = inputs["issue_text"]

    def run(self) -> dict:
        repo = git.Repo(Path.cwd(), search_parent_directories=True)

        original_remote_name = "origin"
        original_remote_url = repo.remotes[original_remote_name].url
        slug = get_slug_from_remote_url(original_remote_url)
        url = self.scm_client.create_issue_comment(slug, self.issue_text, title=self.issue_title)

        return dict(issue_url=url)
