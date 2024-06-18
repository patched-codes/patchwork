from patchwork.common.client.scm import GithubClient, GitlabClient
from patchwork.logger import logger
from patchwork.step import Step


class CreatePRComment(Step):
    required_keys = {"pr_url", "pr_comments"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        if "github_api_key" in inputs.keys():
            self.scm_client = GithubClient(inputs["github_api_key"])
        elif "gitlab_api_key" in inputs.keys():
            self.scm_client = GitlabClient(inputs["gitlab_api_key"])
        else:
            raise ValueError(f'Missing required input data: "github_api_key" or "gitlab_api_key"')

        if "scm_url" in inputs.keys():
            self.scm_client.set_url(inputs["scm_url"])

        self.pr = self.scm_client.get_pr_by_url(inputs["pr_url"])
        self.pr_comments = inputs["pr_comments"]
        self.noisy = bool(inputs.get("noisy_comments", False))

    def run(self) -> dict:
        if not self.noisy:
            self.pr.reset_comments()

        for pr_comment in self.pr_comments:
            comment = self.pr.create_comment(**pr_comment)
            if comment is None:
                logger.error(f"Failed to create comment: {pr_comment}")
            else:
                logger.info(f"Comment created for PR: {self.pr.url}")

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict()
