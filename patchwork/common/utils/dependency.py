import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in __DEPENDENCY_GROUPS.values():
        raise ImportError(f"Module '{name}' is not in allowed dependencies")

    full_name = f"patchworkcli_{name}" if name != "slack_sdk" else "slack_sdk"
    try:
        return importlib.import_module(full_name)
    except ImportError:
        raise ImportError(f"Missing dependency for {name}, please `pip install {name}`")


def chromadb():
    return import_with_dependency_group("chromadb")


def slack_sdk():
    return import_with_dependency_group("slack_sdk")
