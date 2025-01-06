from typing_extensions import List

from patchwork.common.client.scm import AzureDevopsClient, GithubClient, GitlabClient
from patchwork.step import Step
from patchwork.steps.ReadPRDiffs.typed import ReadPRDiffsInputs, ReadPRDiffsOutputs

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


class ReadPRDiffs(Step, input_class=ReadPRDiffsInputs, output_class=ReadPRDiffsOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)

        if "github_api_key" in inputs.keys():
            self.scm_client = GithubClient(inputs["github_api_key"])
        elif "gitlab_api_key" in inputs.keys():
            self.scm_client = GitlabClient(inputs["gitlab_api_key"])
        elif "azuredevops_api_key" in inputs.keys():
            self.scm_client = AzureDevopsClient(inputs["azuredevops_api_key"])
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
