import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    try:
        if name == "chromadb":
            return chromadb()
        raise ImportError(f"Module {name} is not whitelisted")
    except ImportError:
        error_msg = f"Missing dependency for {name}, please `pip install {name}`"
        dependency_group = next(
            (group for group, dependencies in __DEPENDENCY_GROUPS.items() if name in dependencies), None
        )
        if dependency_group is not None:
            error_msg = f"Please `pip install patchwork-cli[{dependency_group}]` to use this step"
        raise ImportError(error_msg)


def chromadb():
    return importlib.import_module("chromadb")
