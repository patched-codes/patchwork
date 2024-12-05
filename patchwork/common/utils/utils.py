from __future__ import annotations

import atexit
import dataclasses
import signal
import tempfile
from pathlib import Path

import tiktoken
from chardet.universaldetector import UniversalDetector
from git import Head, Repo
from typing_extensions import Any, Callable

from patchwork.common.utils.dependency import chromadb
from patchwork.logger import logger
from patchwork.managed_files import HOME_FOLDER

_CLEANUP_FILES: set[Path] = set()


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


class FileWithEncoding:
    """A file-like class that preserves line endings and handles encoding."""
    def __init__(self, file, mode, encoding, errors=None):
        # Default to 'strict' error handling if None provided
        self.binary_file = open(file, mode='rb')
        self.encoding = encoding
        self.errors = 'strict' if errors is None else errors
        self.mode = mode
        self.name = self.binary_file.name
        
    def read(self, size=None):
        data = self.binary_file.read() if size is None else self.binary_file.read(size)
        return data.decode(self.encoding, errors=self.errors)
    
    def write(self, data):
        if isinstance(data, str):
            data = data.encode(self.encoding, errors=self.errors)
        return self.binary_file.write(data)
    
    def close(self):
        self.binary_file.close()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def open_with_chardet(file, mode="r", buffering=-1, errors=None, newline=None, closefd=True, opener=None):
    """Opens a file with automatically detected encoding using chardet while preserving line endings.
    
    Args:
        file: Path to file to open
        mode: Mode to open file in ("r" by default)
        buffering: Buffering policy (-1 by default)
        errors: How to handle encoding errors (None by default)
        newline: How to handle newlines (None by default, which preserves the original line endings)
        closefd: Whether to close the descriptor (True by default)
        opener: Optional opener function (None by default)
    
    Returns:
        A file-like object with the detected encoding that preserves line endings
    """
    detector = UniversalDetector()
    encoding = "utf-8"  # Default encoding if file is empty or detection fails
    
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            detector.feed(chunk)
            if detector.done:
                break

    detector.close()
    if detector.result['encoding'] is not None:
        encoding = detector.result['encoding']
    
    return FileWithEncoding(file, mode, encoding, errors)


_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_openai_tokens(code: str):
    return len(_ENCODING.encode(code))


def get_vector_db_path() -> str:
    CHROMA_DB_PATH = HOME_FOLDER / "chroma.db"
    if CHROMA_DB_PATH:
        return str(CHROMA_DB_PATH)
    else:
        return ".chroma.db"


def openai_embedding_model(
    inputs: dict,
) -> "chromadb.api.types.EmbeddingFunction"["chromadb.api.types.Documents"] | None:
    model = inputs.get(openai_embedding_model.__name__)
    if model is None:
        return None

    api_key = inputs.get("openai_api_key")
    if api_key is None:
        raise ValueError("Missing required input data: 'openai_api_key'")

    return chromadb().utils.embedding_functions.OpenAIEmbeddingFunction(
        api_key=api_key,
        model_name=model,
    )


def huggingface_embedding_model(
    inputs: dict,
) -> "chromadb.api.types.EmbeddingFunction"["chromadb.api.types.Documents"] | None:
    model = inputs.get(huggingface_embedding_model.__name__)
    if model is None:
        return None

    api_key = inputs.get("openai_api_key") or inputs.get("huggingface_api_key")
    if api_key is None:
        raise ValueError("Missing required input data: 'openai_api_key' or 'huggingface_api_key'")

    return chromadb().utils.embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=api_key,
        model_name=model,
    )


_EMBEDDING_FUNCS = [openai_embedding_model, huggingface_embedding_model]

_EMBEDDING_TO_API_KEY_NAME: dict[
    str, Callable[[dict], "chromadb.api.type.EmbeddingFunction"["chromadb.api.types.Documents"] | None]
] = {func.__name__: func for func in _EMBEDDING_FUNCS}


def get_embedding_function(inputs: dict) -> "chromadb.api.types.EmbeddingFunction"["chromadb.api.types.Documents"]:
    embedding_function = next(
        (func(inputs) for input_key, func in _EMBEDDING_TO_API_KEY_NAME.items() if input_key in inputs.keys()),
        chromadb().utils.embedding_functions.SentenceTransformerEmbeddingFunction(),
    )
    if embedding_function is None:
        raise ValueError(f"Missing required input data: one of {_EMBEDDING_TO_API_KEY_NAME.keys()}")

    return embedding_function


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
