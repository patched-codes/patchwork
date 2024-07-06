import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    try:
        if name == "chromadb":
            return chromadb()
        elif name == "slack_sdk":
            return slack_sdk()
        else:
            raise ImportError(f"Missing dependency for {name}, please `pip install {name}`")
    except ImportError as e:
        error_msg = str(e)
        dependency_group = next(
            (group for group, dependencies in __DEPENDENCY_GROUPS.items() if name in dependencies), None
        )
        if dependency_group is not None:
            error_msg = f"Please `pip install patchwork-cli[{dependency_group}]` to use this step"
        raise ImportError(error_msg)


def chromadb():
    return import_with_dependency_group("chromadb")


def slack_sdk():
    return import_with_dependency_group("slack_sdk")
