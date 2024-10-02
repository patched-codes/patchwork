from patchwork.common.client.scm import (
    GithubClient,
    GitlabClient,
    ScmPlatformClientProtocol,
)
from patchwork.step import Step, StepStatus


class CreateIssueComment(Step):
    required_keys = {"issue_url", "issue_text"}

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

        self.issue_text = inputs["issue_text"]
        self.issue_url = inputs["issue_url"]

    def run(self) -> dict:
        try:
            slug, issue_id = self.scm_client.get_slug_and_id_from_url(self.issue_url)
            url = self.scm_client.create_issue_comment(slug, self.issue_text, issue_id=issue_id)
        except Exception as e:
            self.set_status(StepStatus.FAILED, f"Failed to create issue comment")
            raise e

        return dict(issue_comment_url=url)
