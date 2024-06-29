from functools import lru_cache
import chromadb
import semgrep
import depscan
import slack_sdk

__DEPENDENCY_GROUPS = {
    "rag": [chromadb],
    "security": [semgrep, depscan],
    "notification": [slack_sdk],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name == "chromadb":
        return chromadb
    elif name == "semgrep":
        return semgrep
    elif name == "depscan":
        return depscan
    elif name == "slack_sdk":
        return slack_sdk
    else:
        raise ImportError(f"Missing dependency for {name}, please `pip install {name}`")


def chromadb():
    return import_with_dependency_group("chromadb")


def slack_sdk():
    return import_with_dependency_group("slack_sdk")
