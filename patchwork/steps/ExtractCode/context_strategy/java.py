from typing import Tuple

from tree_sitter_languages import get_language, get_parser

from .protocol import ContextStrategyProtocol


class JavaStrategy(ContextStrategyProtocol):
    def __init__(self, query: str):
        self.query = query

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int | None, int | None]:
        language = get_language("java")
        java_parser = get_parser("java")
        tree = java_parser.parse("".join(src).encode("utf-8-sig"))
        query_result = language.query(self.query).captures(tree.root_node)

        for node, name in query_result:
            if node.start_point[0] <= start and end <= node.end_point[0]:
                return node.start_point[0], node.end_point[0] + 1

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
