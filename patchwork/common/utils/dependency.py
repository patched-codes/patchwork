import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    try:
        for dependencies in __DEPENDENCY_GROUPS.values():
            if name in dependencies:
                return importlib.import_module(name)
        raise ImportError("Module not in whitelist")
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
