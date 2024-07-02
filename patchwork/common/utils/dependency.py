import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
}

VALID_MODULES = {
    "chromadb": "chromadb",
    "semgrep": "patchwork-cli[security]",
    "depscan": "patchwork-cli[security]",
}

@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in VALID_MODULES:
        raise ImportError(f"Module {name} is not allowed to be imported")
    
    try:
        return importlib.import_module(VALID_MODULES[name])
    except ImportError:
        raise ImportError(f"Missing dependency for {name}, please `pip install {VALID_MODULES[name]}`")

def chromadb():
    return import_with_dependency_group("chromadb")
