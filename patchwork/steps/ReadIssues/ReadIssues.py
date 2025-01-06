from patchwork.common.client.scm import (
    GithubClient,
    GitlabClient,
    ScmPlatformClientProtocol,
)
from patchwork.step import Step


class ReadIssues(Step):
    required_keys = {"issue_url"}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.scm_client: ScmPlatformClientProtocol
        if "github_api_key" in inputs.keys():
            self.scm_client = GithubClient(inputs["github_api_key"])
        elif "gitlab_api_key" in inputs.keys():
            self.scm_client = GitlabClient(inputs["gitlab_api_key"])
        else:
            raise ValueError(f'Missing required input data: "github_api_key" or "gitlab_api_key"')

        if "scm_url" in inputs.keys():
            self.scm_client.set_url(inputs["scm_url"])

        self.issue = self.scm_client.find_issue_by_url(inputs["issue_url"])
        if not self.issue:
            raise ValueError(f"Could not find issue with url: {inputs['issue_url']}")

    def run(self) -> dict:
        return dict(
            issue_title=self.issue.get("title"),
            issue_body=self.issue.get("body"),
            issue_comments=self.issue.get("comments"),
            issue_description=f"""\
Title:
{self.issue.get("title")}

Description:
{self.issue.get("body")}
""",
        )
