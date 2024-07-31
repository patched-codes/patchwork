from pathlib import Path

import git
from git.exc import GitCommandError

from patchwork.common.client.scm import (
    GithubClient,
    GitlabClient,
    ScmPlatformClientProtocol,
    get_slug_from_remote_url,
)
from patchwork.logger import logger
from patchwork.step import Step


class CreatePR(Step):
    required_keys = {"target_branch"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.enabled = not bool(inputs.get("disable_pr", False))
        if self.enabled:
            self.scm_client = None
            if "github_api_key" in inputs.keys():
                self.scm_client = GithubClient(inputs["github_api_key"])
            elif "gitlab_api_key" in inputs.keys():
                self.scm_client = GitlabClient(inputs["gitlab_api_key"])
            else:
                logger.warning(
                    f'Missing required input data: "github_api_key" or "gitlab_api_key",'
                    f" PR creation will be disabled."
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

    def run(self) -> dict:
        if not self.enabled:
            logger.warning(f"PR creation is disabled. Skipping PR creation.")
            return dict()

        repo = git.Repo(Path.cwd(), search_parent_directories=True)

        original_remote_name = "origin"
        push_args = ["--set-upstream", original_remote_name, self.target_branch]
        if self.force:
            push_args.insert(0, "--force")

        push(repo, push_args)
        logger.debug(f"Pushed to {original_remote_name}/{self.target_branch}")

        logger.info(f"Creating PR from {self.base_branch} to {self.target_branch}")
        original_remote_url = repo.remotes[original_remote_name].url
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
        logger.info(f"Run completed {self.__class__.__name__}")
        return {"pr_url": url}


def push(repo: git.Repo, args):
    repo_git = repo.git
    try:
        with repo_git.custom_environment(GIT_TERMINAL_PROMPT="0"):
            repo_git.push(*args)
    except GitCommandError:
        with logger.freeze():
            repo_git.push(*args)


def create_pr(
    repo_slug: str,
    body: str,
    title: str,
    base_branch_name: str,
    target_branch_name: str,
    scm_client: ScmPlatformClientProtocol,
    force: bool = False,
):
    pr = scm_client.find_pr(repo_slug, base_branch_name, target_branch_name)
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
