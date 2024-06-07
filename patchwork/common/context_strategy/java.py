from tree_sitter_languages import get_language, get_parser
from typing_extensions import Tuple

from .protocol import ContextStrategyProtocol


class JavaStrategy(ContextStrategyProtocol):
    def __init__(self, query: str):
        self.query = query

    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        language = get_language("java")
        java_parser = get_parser("java")
        tree = java_parser.parse("".join(src).encode("utf-8-sig"))
        query_result = language.query(self.query).captures(tree.root_node)

        return [(node.start_point[0], node.end_point[0] + 1) for node, name in query_result]

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int | None, int | None]:
        for context_start, context_end in self.get_contexts(src):
            if context_start <= start and end <= context_end - 1:
                return context_start, context_end

        return None, None

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        return filename.endswith(".java") and len(src) > 0


class JavaClassStrategy(JavaStrategy):
    def __init__(self):
        super().__init__(
            """
        [
            (class_declaration) @class
        ]
        """.strip()
        )


class JavaMethodStrategy(JavaStrategy):
    def __init__(self):
        super().__init__(
            """
        [
            (method_declaration) @method
        ]
        """.strip()
        )


class JavaBlockStrategy(JavaStrategy):
    def __init__(self):
        super().__init__(
            """
        [
            (block) @block
        ]
        """.strip()
        )
