from patchwork.common.client.scm import (
    GithubClient,
    GitlabClient,
    ScmPlatformClientProtocol,
)
from patchwork.logger import logger
from patchwork.step import Step


class ReadIssues(Step):
    required_keys = {"issue_url"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.scm_client: ScmPlatformClientProtocol
        if "github_api_key" in inputs.keys():
            try:
                self.scm_client = GithubClient(inputs["github_api_key"])
            except Exception as e:
                logger.error(e)
        elif "gitlab_api_key" in inputs.keys():
            try:
                self.scm_client = GitlabClient(inputs["gitlab_api_key"])
            except Exception as e:
                logger.error(e)
        else:
            return

        if "scm_url" in inputs.keys():
            self.scm_client.set_url(inputs["scm_url"])

        try:
            self.issue_texts = self.scm_client.find_issue_by_url(inputs["issue_url"])
        except Exception as e:
            logger.error(e)

    def run(self) -> dict:
        return dict(issue_text=[self.issue_texts[0]])
