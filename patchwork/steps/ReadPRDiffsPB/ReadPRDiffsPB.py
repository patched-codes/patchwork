from typing import List

from patchwork.common.client.scm import GithubClient, GitlabClient
from patchwork.step import Step

_IGNORED_EXTENSIONS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx",
    ".zip",
    ".tar",
    ".gz",
    ".lock",
]


def filter_by_extension(file, extensions):
    return any(file.endswith(ext) for ext in extensions)


class ReadPRDiffsPB(Step):
    required_keys = {"pr_url"}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
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

    def run(self) -> dict:
        pr_texts = self.pr.texts()
        title = pr_texts.get("title", "")
        body = pr_texts.get("body", "")
        comments = pr_texts.get("comments", [])
        diffs: List[dict] = []
        for path, diff_text in pr_texts.get("diffs", {}).items():
            if filter_by_extension(path, _IGNORED_EXTENSIONS):
                continue
            diffs.append(dict(path=path, diff=diff_text))

        return dict(title=title, body=body, comments=comments, diffs=diffs)
