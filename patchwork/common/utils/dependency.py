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
        if name in __DEPENDENCY_GROUPS:
            return importlib.import_module(name)
        else:
            raise ImportError(f"Module {name} is not in the whitelist")
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
