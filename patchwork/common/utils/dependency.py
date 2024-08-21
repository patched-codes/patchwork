import importlib.util
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    try:
        module_info = importlib.util.find_spec(name)
        if module_info is None:
            raise ImportError
        return importlib.util.module_from_spec(module_info)
    except ImportError:
        error_msg = f"Missing dependency for {name}, please `pip install {name}`"
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
