import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}

__ALLOWED_MODULES = {"semgrep", "depscan", "slack_sdk"}

@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in __ALLOWED_MODULES:
        raise ImportError(f"Module {name} is not allowed.")
    try:
        return importlib.import_module(name)
    except ImportError:
        error_msg = f"Missing dependency for {name}, please `pip install {name}`"
        dependency_group = next(
            (group for group, dependencies in __DEPENDENCY_GROUPS.items() if name in dependencies), None
        )
        if dependency_group is not None:
            error_msg = f"Please `pip install patchwork-cli[{dependency_group}]` to use this step"
        raise ImportError(error_msg)

def slack_sdk():
    return import_with_dependency_group("slack_sdk")
