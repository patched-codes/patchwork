import importlib
from functools import lru_cache

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    if name not in __DEPENDENCY_GROUPS:
        raise ImportError(f"Unknown dependency group for {name}")
    
    dependencies = __DEPENDENCY_GROUPS[name]
    for dependency in dependencies:
        globals()[dependency] = importlib.import_module(dependency)

    return globals()[name]


def chromadb():
    return import_with_dependency_group("chromadb")
