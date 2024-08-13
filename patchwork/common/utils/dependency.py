import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in __DEPENDENCY_GROUPS.keys():
        raise ImportError(f"Missing dependency for {name}, please `pip install {name}`")
    
    try:
        return importlib.import_module(name)
    except ImportError:
        dependency_group = next(
            (group for group, dependencies in __DEPENDENCY_GROUPS.items() if name in dependencies), None
        )
        if dependency_group is not None:
            raise ImportError(f"Please `pip install patchwork-cli[{dependency_group}]` to use this step")


def chromadb():
    return import_with_dependency_group("chromadb")


def slack_sdk():
    return import_with_dependency_group("slack_sdk")
