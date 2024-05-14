from tree_sitter_languages import get_language, get_parser
from typing_extensions import Tuple

from .protocol import ContextStrategyProtocol


class JavascriptContextStrategy(ContextStrategyProtocol):
    def __init__(self, language: str, query: str, exts: list[str]):
        self.language = language
        self.query = query
        self.exts = exts

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int | None, int | None]:
        language = get_language(self.language)
        parser = get_parser(self.language)
        tree = parser.parse("".join(src).encode("utf-8-sig"))
        query_result = language.query(self.query).captures(tree.root_node)

        for node, name in query_result:
            if node.start_point[0] <= start and end <= node.end_point[0]:
                return node.start_point[0], node.end_point[0] + 1

        return None, None

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        return any(filename.endswith(ext) for ext in self.exts) and len(src) > 0


_javascript_language = "typescript"
_jsx_language = "tsx"

_class_query = """
    [
        (class_declaration) @class
        (interface_declaration) @interface
        (enum_declaration) @enum
    ]
""".strip()
_function_query = """
        [
            (function_declaration) @function
        ]
    """.strip()
_block_query = """
        [
            (statement_block) @block
        ]
    """.strip()

_javascript_exts = [".js", ".ts"]
_jsx_exts = [".jsx", ".tsx"]


class JavascriptClassStrategy(JavascriptContextStrategy):
    def __init__(self):
        super().__init__(_javascript_language, _class_query, _javascript_exts)


class JavascriptFunctionStrategy(JavascriptContextStrategy):
    def __init__(self):
        super().__init__(_javascript_language, _function_query, _javascript_exts)


class JavascriptBlockStrategy(JavascriptContextStrategy):
    def __init__(self):
        super().__init__(_javascript_language, _block_query, _javascript_exts)


class JsxClassStrategy(JavascriptContextStrategy):
    def __init__(self):
        super().__init__(_jsx_language, _class_query, _jsx_exts)


class JsxFunctionStrategy(JavascriptContextStrategy):
    def __init__(self):
        super().__init__(_jsx_language, _function_query, _jsx_exts)


class JsxBlockStrategy(JavascriptContextStrategy):
    def __init__(self):
        super().__init__(_jsx_language, _block_query, _jsx_exts)
