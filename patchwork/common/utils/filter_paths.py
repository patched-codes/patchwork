from __future__ import annotations

from fnmatch import fnmatch
from pathlib import Path

import git

IGNORE_DIRS = {
    ".git",
    ".idea",
    "__pycache__",
    ".mvn",
    "node_modules",
}

IGNORE_EXTS_GLOBS = {
    "*.pyc",
    "*.pyo",
    "*.pyd",
    "*.whl",
    "*.egg",
    "*.egg-info",
    "*.dist-info",
}

IGNORE_FILES_GLOBS = {
    "requirements.txt",
    "requirements-dev.txt",
    "requirements-test.txt",
    "mvnw",
    "mvnw.cmd",
    "gradlew",
    "gradlew.bat",
}


class PathFilter:
    def __init__(
        self, *, base_path: str | Path = Path.cwd(), ignored_groks: set[str] | None = None, max_depth: int = -1
    ):
        self.base_path = Path(base_path)
        self.max_depth = max_depth
        self.__ignored_groks = ignored_groks if ignored_groks is not None else set()
        try:
            self.__repo = git.Repo(base_path, search_parent_directories=True)
            self.__ignored_groks.update(self.__get_gitignore_ignored_groks())
        except git.InvalidGitRepositoryError:
            self.__repo = None

    def __get_gitignore_ignored_groks(self) -> set[str]:
        ignored_groks = set()
        gitignore_file = Path(self.__repo.working_tree_dir) / ".gitignore"
        if not gitignore_file.is_file():
            return ignored_groks
        lines = gitignore_file.read_text().splitlines()
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith("#") or stripped_line == "":
                continue
            ignored_groks.add(stripped_line)
        return ignored_groks

    def get_grok_ignored(self, file_to_test: str | Path) -> str | None:
        """
        Get the grok string that causes the file to be ignored

        :param file_to_test: file to test if it is ignored because of depth level
        :return: Grok string if the file is ignored else None
        """
        file = Path(file_to_test)
        paths_to_test = [file] + list(file.parents)
        for ignored_grok in self.__ignored_groks:
            for path in paths_to_test:
                if fnmatch(str(path), ignored_grok):
                    return ignored_grok
        return None

    def get_depth_ignored(self, file_to_test: str | Path) -> int | None:
        """
        Get depth of file that causes the file to be ignored.

        :param file_to_test: file to test if it is ignored because of depth level
        :return: Depth of file if the file is ignored else None.
        """
        if self.max_depth == -1:
            return None

        file = Path(file_to_test)

        try:
            file_depth = len(file.relative_to(self.base_path).parts)
        except ValueError:
            return None

        if file_depth > self.max_depth:
            return file_depth

        return None
