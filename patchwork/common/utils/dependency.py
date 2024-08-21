import importlib
from functools import lru_cache

ALLOWED_MODULES = ["chromadb", "semgrep", "depscan", "slack_sdk"]

@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in ALLOWED_MODULES:
        raise ImportError(f"Module {name} is not allowed to be imported.")
        
    try:
        return importlib.import_module(name)
    except ImportError:
        error_msg = f"Missing dependency for {name}, please `pip install {name}`"
        raise ImportError(error_msg)

def chromadb():
    return import_with_dependency_group("chromadb")

def slack_sdk():
    return import_with_dependency_group("slack_sdk")
