from __future__ import annotations

import itertools
from pathlib import Path
from typing import Iterable

# switch to pure globs once https://github.com/python/cpython/issues/73435 is resolved
IGNORE_DIRS = {
    ".git",
    ".idea",
    "__pycache__",
    ".mvn",
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


def is_ignored(file_path: Path, ignored_dirs: Iterable[str] | None = None, *globs: Iterable[str]) -> bool:
    final_ignore_globs = globs if globs else itertools.chain(IGNORE_EXTS_GLOBS, IGNORE_FILES_GLOBS)
    final_ignored_dirs = ignored_dirs if ignored_dirs else IGNORE_DIRS
    return any(file_path.match(ignore_glob) for ignore_glob in final_ignore_globs) or any(
        ignore_dir in file_path.parts[:-1] for ignore_dir in final_ignored_dirs
    )
