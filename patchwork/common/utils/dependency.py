from functools import lru_cache
import chromadb

__DEPENDENCY_GROUPS = {
    "rag": ["chromadb"],
    "security": ["semgrep", "depscan"],
}


@lru_cache(maxsize=None)
def import_with_dependency_group(name):
    return getattr(chromadb, name)


def chromadb():
    return import_with_dependency_group("chromadb")
