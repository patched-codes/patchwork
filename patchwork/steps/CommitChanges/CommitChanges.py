from __future__ import annotations

import contextlib
from pathlib import Path

import git
from git import Repo
from typing_extensions import Generator

from patchwork.common.utils.filter_paths import PathFilter
from patchwork.common.utils.utils import get_current_branch
from patchwork.logger import logger
from patchwork.step import Step, StepStatus


@contextlib.contextmanager
def transitioning_branches(
    repo: Repo, branch_prefix: str, branch_suffix: str = "", force: bool = True, enabled: bool = True
) -> Generator[tuple[str, str], None, None]:
    if not enabled:
        from_branch = get_current_branch(repo)
        from_branch_name = from_branch.name if not from_branch.is_remote() else from_branch.remote_head
        yield from_branch_name, from_branch_name
        return

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
            "--no-verify",
            "--author",
            "patched.codes[bot]<298395+patched.codes[bot]@users.noreply.github.com>",
            "-m",
            msg,
        )


class CommitChanges(Step):
    required_keys = {"modified_code_files"}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.enabled = not bool(inputs.get("disable_branch"))

        self.modified_code_files = inputs["modified_code_files"]
        if len(self.modified_code_files) < 1:
            logger.warn("No modified files to commit changes for.")
            self.enabled = False

        self.force = inputs.get("force_branch_creation", True)
        self.branch_prefix = inputs.get("branch_prefix", "patchwork-")
        self.branch_suffix = inputs.get("branch_suffix", "")
        if self.enabled and self.branch_prefix == "" and self.branch_suffix == "":
            raise ValueError("Both branch_prefix and branch_suffix cannot be empty")

    def __get_repo_tracked_modified_files(self, repo: Repo) -> set[Path]:
        repo_dir_path = Path(repo.working_tree_dir)
        path_filter = PathFilter(base_path=repo.working_tree_dir)

        repo_changed_files = set()
        for item in repo.index.diff(None):
            repo_changed_file = Path(item.a_path)
            possible_ignored_grok = path_filter.get_grok_ignored(repo_changed_file)
            if possible_ignored_grok is not None:
                logger.warn(f'Ignoring file: {item.a_path} because of "{possible_ignored_grok}" in .gitignore file.')
                continue
            repo_changed_files.add(repo_dir_path / repo_changed_file)

        return repo_changed_files

    def run(self) -> dict:
        cwd = Path.cwd()
        repo = git.Repo(cwd, search_parent_directories=True)
        repo_dir_path = Path(repo.working_tree_dir)
        repo_changed_files = self.__get_repo_tracked_modified_files(repo)
        repo_untracked_files = {repo_dir_path / item for item in repo.untracked_files}
        modified_files = {Path(modified_code_file["path"]).resolve() for modified_code_file in self.modified_code_files}
        true_modified_files = modified_files.intersection(repo_changed_files.union(repo_untracked_files))
        if len(true_modified_files) < 1:
            self.set_status(
                StepStatus.SKIPPED, "No file found to add, commit and push. Branch creation will be disabled."
            )
            from_branch = get_current_branch(repo)
            from_branch_name = from_branch.name if not from_branch.is_remote() else from_branch.remote_head
            return dict(target_branch=from_branch_name)

        with transitioning_branches(
            repo,
            branch_prefix=self.branch_prefix,
            branch_suffix=self.branch_suffix,
            force=self.force,
            enabled=self.enabled,
        ) as (
            from_branch,
            to_branch,
        ):
            for modified_file in true_modified_files:
                repo.git.add(modified_file)
                commit_with_msg(repo, f"Patched {modified_file.relative_to(repo_dir_path)}")

            return dict(
                base_branch=from_branch,
                target_branch=to_branch,
            )
