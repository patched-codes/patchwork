from __future__ import annotations

import atexit
import dataclasses
import random
import signal
import string
import tempfile
from collections.abc import Mapping
from pathlib import Path

import chevron
import tiktoken
from chardet.universaldetector import UniversalDetector
from git import Head, Repo
from typing_extensions import Any, Callable, Counter

from patchwork.logger import logger

_CLEANUP_FILES: set[Path] = set()
_NEWLINES = {"\n", "\r\n", "\r"}


def mustache_render(template: str, data: Mapping) -> str:
    if len(data.keys()) < 1:
        return template

    chevron.render.__globals__["_html_escape"] = lambda x: x
    return chevron.render(
        template=template,
        data=data,
        partials_path=None,
        partials_ext="".join(random.choices(string.ascii_uppercase + string.digits, k=32)),
        partials_dict=dict(),
    )


def detect_newline(path: str | Path) -> str | None:
    with open(path, "r", newline="") as f:
        lines = f.read().splitlines(keepends=True)
    if len(lines) < 1:
        return None

    counter = Counter(_NEWLINES)
    for line in lines:
        newline_len = 0
        newline = "\n"
        for possible_newline in _NEWLINES:
            if line.endswith(possible_newline) and len(possible_newline) > newline_len:
                newline_len = len(possible_newline)
                newline = possible_newline
        counter[newline] += 1
    return counter.most_common(1)[0][0]


def _cleanup_files():
    for file in _CLEANUP_FILES:
        file.unlink(missing_ok=True)


def _cleanup_handler(prev_handler: Callable):
    def inner(*args):
        _cleanup_files()
        return prev_handler

    return inner


for sig in [signal.SIGINT, signal.SIGTERM]:
    prev_handler = signal.getsignal(sig)
    signal.signal(sig, _cleanup_handler(prev_handler))

atexit.register(_cleanup_files)


def defered_temp_file(
    mode="w+b", buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None
):
    tempfile_fp = tempfile.NamedTemporaryFile(
        mode=mode,
        buffering=buffering,
        encoding=encoding,
        newline=newline,
        suffix=suffix,
        prefix=prefix,
        dir=dir,
        errors=errors,
        delete=False,
    )

    _CLEANUP_FILES.add(Path(tempfile_fp.name))
    return tempfile_fp


def open_with_chardet(file, mode="r", buffering=-1, errors=None, newline=None, closefd=True, opener=None):
    detector = UniversalDetector()
    with open(
        file=file, mode="rb", buffering=buffering, errors=errors, newline=newline, closefd=closefd, opener=opener
    ) as f:
        while True:
            line = f.read(1024)
            if not line:
                break
            detector.feed(line)
            if detector.done:
                break

    detector.close()

    encoding = detector.result.get("encoding", "utf-8")
    return open(
        file=file,
        mode=mode,
        buffering=buffering,
        encoding=encoding,
        errors=errors,
        newline=newline,
        closefd=closefd,
        opener=opener,
    )


_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_openai_tokens(code: str):
    return len(_ENCODING.encode(code))


def get_current_branch(repo: Repo) -> Head:
    remote = repo.remote("origin")
    if repo.head.is_detached:
        from_branch = next(
            (branch for branch in remote.refs if branch.commit == repo.head.commit and branch.remote_head != "HEAD"),
            None,
        )
    else:
        from_branch = repo.active_branch

    if from_branch is None:
        raise ValueError(
            "Could not determine the current branch."
            "Make sure repository is not in a detached HEAD state with additional commits."
        )

    return from_branch


def is_container() -> bool:
    test_files = ["/.dockerenv", "/run/.containerenv"]
    if any(Path(file).exists() for file in test_files):
        return True

    cgroup_v1 = Path("/proc/self/cgroup")
    if cgroup_v1.exists():
        with cgroup_v1.open() as f:
            lines = f.readlines()
            for line in lines:
                # format is `hierachy_id:controllers:pathname`
                # cgroup v2 is `0::/`
                hierachy_id, _, rest = line.partition(":")
                controllers, _, pathname = rest.partition(":")
                if hierachy_id != "0" and len(controllers) > 0:
                    return True

    # TODO: cgroup v2 detection
    return False


def exclude_none_dict(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}


@dataclasses.dataclass
class RetryData:
    retry_limit: int
    retry_count: int


def retry(callback: Callable[[RetryData], Any], retry_limit=3) -> Any:
    for i in range(retry_limit):
        retry_count = i + 1
        try:
            return callback(RetryData(retry_limit=retry_limit, retry_count=retry_count))
        except Exception as e:
            logger.error(f"Retry {retry_count} failed with error: {e}")
            if retry_count == retry_limit:
                raise e
