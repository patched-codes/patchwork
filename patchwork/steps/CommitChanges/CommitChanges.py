import contextlib
from pathlib import Path

import git
from git import Repo
from typing_extensions import Generator

from patchwork.common.utils import get_current_branch
from patchwork.logger import logger
from patchwork.step import Step


def get_slug_from_remote_url(remote_url: str) -> str:
    # TODO: consider using https://github.com/nephila/giturlparse instead
    if remote_url.startswith("git@"):
        # ssh
        _, _, potential_slug = remote_url.partition(":")
    else:
        potential_slug = "/".join(remote_url.split("/")[-2:])

    return potential_slug.removesuffix(".git")


@contextlib.contextmanager
def transitioning_branches(
    repo: Repo, branch_prefix: str, branch_suffix: str = "", force: bool = True
) -> Generator[tuple[str, str], None, None]:
    from_branch = get_current_branch(repo)
    from_branch_name = from_branch.name if not from_branch.is_remote() else from_branch.remote_head
    next_branch_name = f"{branch_prefix}{from_branch_name}{branch_suffix}"
    if next_branch_name in repo.heads and not force:
        raise ValueError(f'Local Branch "{next_branch_name}" already exists.')
    if next_branch_name in repo.remote("origin").refs and not force:
        raise ValueError(f'Remote Branch "{next_branch_name}" already exists.')

    logger.info(f'Creating new branch "{next_branch_name}".')
    to_branch = repo.create_head(next_branch_name, force=force)

    try:
        to_branch.checkout()
        yield from_branch_name, next_branch_name
    finally:
        from_branch.checkout()


class _EphemeralGitConfig:
    _DEFAULT = -2378137912

    def __init__(self, repo: Repo):
        self._repo = repo
        self._keys: set[tuple[str, str]] = set()
        self._original_values: dict[tuple[str, str], str] = dict()
        self._modified_values: dict[tuple[str, str], str] = dict()

    def set_value(self, section: str, option: str, value: str):
        self._keys.add((section, option))
        self._modified_values[(section, option)] = value

    @contextlib.contextmanager
    def context(self):
        try:
            self._persist_values_to_be_modified()
            yield
        finally:
            self._undo_modified_values()

    def _persist_values_to_be_modified(self):
        reader = self._repo.config_reader("repository")
        for section, option in self._keys:
            original_value = reader.get_value(section, option, self._DEFAULT)
            if original_value != self._DEFAULT:
                self._original_values[(section, option)] = original_value

        writer = self._repo.config_writer()
        try:
            for section, option in self._keys:
                writer.set_value(section, option, self._modified_values[(section, option)])
        finally:
            writer.release()

    def _undo_modified_values(self):
        writer = self._repo.config_writer()
        try:
            for section, option in self._keys:
                original_value = self._original_values.get((section, option), None)
                if original_value is None:
                    writer.remove_option(section, option)
                else:
                    writer.set_value(section, option, original_value)
        finally:
            writer.release()


def commit_with_msg(repo: Repo, msg: str):
    ephemeral = _EphemeralGitConfig(repo)
    ephemeral.set_value("user", "name", "patched.codes[bot]")
    ephemeral.set_value("user", "email", "298395+patched.codes[bot]@users.noreply.github.com")

    with ephemeral.context():
        repo.git.commit(
            "--author",
            "patched.codes[bot]<298395+patched.codes[bot]@users.noreply.github.com>",
            "-m",
            msg,
        )


class CommitChanges(Step):
    required_keys = {"modified_code_files"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.enabled = not bool(inputs.get("disable_branch"))

        self.modified_code_files = inputs["modified_code_files"]
        if len(self.modified_code_files) < 1:
            logger.warn("No modified files to commit changes for.")
            self.enabled = False

        self.force = inputs.get("force_branch_creation", True)
        self.branch_prefix = inputs.get("branch_prefix", "")
        self.branch_suffix = inputs.get("branch_suffix", "")
        if self.enabled and self.branch_prefix == "" and self.branch_suffix == "":
            raise ValueError("Both branch_prefix and branch_suffix cannot be empty")

    def run(self) -> dict:
        repo = git.Repo(Path.cwd(), search_parent_directories=True)
        if not self.enabled:
            logger.debug("Branch creation is disabled.")
            from_branch = get_current_branch(repo)
            from_branch_name = from_branch.name if not from_branch.is_remote() else from_branch.remote_head
            return dict(target_branch=from_branch_name)

        modified_files = {modified_code_file["path"] for modified_code_file in self.modified_code_files}

        with transitioning_branches(
            repo, branch_prefix=self.branch_prefix, branch_suffix=self.branch_suffix, force=self.force
        ) as (
            from_branch,
            to_branch,
        ):
            for modified_file in modified_files:
                repo.git.add(modified_file)
                commit_with_msg(repo, f"Patched {modified_file}")

            logger.info(f"Run completed {self.__class__.__name__}")
            return dict(
                base_branch=from_branch,
                target_branch=to_branch,
            )
