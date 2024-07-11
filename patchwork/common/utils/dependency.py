import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}

def safe_import_module(name):
    if name == "chromadb":
        return importlib.import_module("chromadb")
    elif name == "slack_sdk":
        return importlib.import_module("slack_sdk")
    else:
        raise ImportError(f"Module {name} not found")

@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    try:
        return safe_import_module(name)
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
