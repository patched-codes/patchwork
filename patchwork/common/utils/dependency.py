import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
    "notification": ["slack_sdk"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in __DEPENDENCY_GROUPS:
        raise ImportError(f"Missing dependency for {name}, please `pip install {name}`")
        
    dependencies = __DEPENDENCY_GROUPS[name]
    return importlib.import_module(name)


def chromadb():
    return import_with_dependency_group("chromadb")


def slack_sdk():
    return import_with_dependency_group("slack_sdk")
