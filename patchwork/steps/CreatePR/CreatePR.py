from pathlib import Path

import git
from git.exc import GitCommandError

from patchwork.common.client.scm import (
    AzureDevopsClient,
    GithubClient,
    GitlabClient,
    ScmPlatformClientProtocol,
    get_slug_from_remote_url,
)
from patchwork.logger import logger
from patchwork.step import Step, StepStatus


class CreatePR(Step):
    required_keys = {"target_branch"}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.original_remote_name = "origin"

        self.enabled = not bool(inputs.get("disable_pr", False))
        if self.enabled:
            self.scm_client = None
            if "github_api_key" in inputs.keys():
                self.scm_client = GithubClient(inputs["github_api_key"])
            elif "gitlab_api_key" in inputs.keys():
                self.scm_client = GitlabClient(inputs["gitlab_api_key"])
            elif "azuredevops_api_key" in inputs.keys():
                self.scm_client = AzureDevopsClient(inputs["azuredevops_api_key"])
            else:
                logger.warning(
                    f'Missing required input data: "github_api_key", "gitlab_api_key" or "azuredevops_api_key". '
                    f"PR creation will be disabled."
                )
                self.enabled = False

        if self.enabled:
            if "scm_url" in inputs.keys():
                self.scm_client.set_url(inputs["scm_url"])

            if not self.scm_client.test():
                logger.warning(
                    f"{self.scm_client.__class__.__name__} token test failed. " f"PR creation will be disabled."
                )
                self.enabled = False

        self.pr_body = inputs.get("pr_body", "")
        self.title = inputs.get("pr_title", "Patchwork PR")
        self.force = bool(inputs.get("force_pr_creation", False))
        self.base_branch = inputs.get("base_branch")
        if self.enabled and self.base_branch is None:
            logger.warn("Base branch not provided. Skipping PR creation.")
            self.enabled = False
        self.target_branch = inputs["target_branch"]
        if self.enabled and self.base_branch == self.target_branch:
            logger.warn("Base branch and target branch are the same. Skipping PR creation.")
            self.enabled = False

    def __push(self, repo):
        push_args = ["--set-upstream", self.original_remote_name, self.target_branch]
        if self.force:
            push_args.insert(0, "--force")

        is_push_success = push(repo, push_args)
        logger.debug(f"Pushed to {self.original_remote_name}/{self.target_branch}")
        return is_push_success

    def run(self) -> dict:
        repo = git.Repo(Path.cwd(), search_parent_directories=True)
        if not self.enabled:
            if (
                self.base_branch == self.target_branch
                and len(list(repo.iter_commits(f"{self.target_branch}@{{u}}..{self.target_branch}"))) > 0
            ):
                is_push_success = self.__push(repo)
                if not is_push_success:
                    self.set_status(
                        StepStatus.FAILED,
                        f"Failed to push to {self.original_remote_name}/{self.target_branch}. Skipping PR creation.",
                    )
                return dict()

            self.set_status(StepStatus.WARNING, "PR creation is disabled. Skipping PR creation.")
            logger.warning(f"PR creation is disabled. Skipping PR creation.")
            return dict()

        is_push_success = self.__push(repo)
        if not is_push_success:
            self.set_status(
                StepStatus.FAILED,
                f"Failed to push to {self.original_remote_name}/{self.target_branch}. Skipping PR creation.",
            )
            return dict()

        logger.info(f"Creating PR from {self.base_branch} to {self.target_branch}")
        original_remote_url = repo.remotes[self.original_remote_name].url
        repo_slug = get_slug_from_remote_url(original_remote_url)
        url = create_pr(
            repo_slug=repo_slug,
            title=self.title,
            body=self.pr_body,
            base_branch_name=self.base_branch,
            target_branch_name=self.target_branch,
            scm_client=self.scm_client,
            force=self.force,
        )

        logger.info(f"[green]PR created at [link={url}]{url}[/link][/]", extra={"markup": True})
        return {"pr_url": url}


def push(repo: git.Repo, args) -> bool:
    try:
        with repo.git.custom_environment(GIT_TERMINAL_PROMPT="0"):
            repo.git.push(*args)
        return True
    except GitCommandError as e:
        logger.error("Git command failed with:")
        logger.error(e.stdout)
        logger.error(e.stderr)

    freeze_func = getattr(logger, "freeze", None)
    if freeze_func is None:
        return False

    try:
        with logger.freeze():
            repo.git.push(*args)
        return True
    except GitCommandError as e:
        logger.error("Git command failed with:")
        logger.error(e.stdout)
        logger.error(e.stderr)

    return False


def create_pr(
    repo_slug: str,
    body: str,
    title: str,
    base_branch_name: str,
    target_branch_name: str,
    scm_client: ScmPlatformClientProtocol,
    force: bool = False,
):
    prs = scm_client.find_prs(repo_slug, original_branch=base_branch_name, feature_branch=target_branch_name)
    pr = next(iter(prs), None)
    if pr is None:
        pr = scm_client.create_pr(
            repo_slug,
            title,
            body,
            base_branch_name,
            target_branch_name,
        )

        pr.set_pr_description(body)

        return pr.url()

    if force:
        pr.set_pr_description(body)
        return pr.url()

    logger.error(
        f"PR with the same base branch, {base_branch_name}, and target branch, {target_branch_name},"
        f" already exists. Skipping PR creation."
    )
    return ""
