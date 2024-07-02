import importlib
from functools import lru_cache

__DEPENDENCY_MODULES = {
    "rag": "chromadb",
    "security": "semgrep",
    "notification": "slack_sdk",
}

@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    try:
        module_name = __DEPENDENCY_MODULES.get(name)
        if module_name:
            return importlib.import_module(module_name)
        else:
            raise ImportError(f"Module name for {name} is not found")
    except ImportError as e:
        raise ImportError(f"Missing dependency for {name}, please `pip install {name}`") from e

def chromadb():
    return import_with_dependency_group("rag")

def slack_sdk():
    return import_with_dependency_group("notification")
