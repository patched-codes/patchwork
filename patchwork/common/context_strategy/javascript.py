from tree_sitter_languages import get_language, get_parser
from typing_extensions import Tuple

from patchwork.common.context_strategy.protocol import TreeSitterStrategy


_javascript_language = "typescript"
_jsx_language = "tsx"

_class_query = """
    [
        (class_declaration)
        (interface_declaration)
        (enum_declaration)
    ] @node
""".strip()
_function_query = """
    [
      (comment) @comment
      [
        ( function )
        ( function_declaration )
        ( generator_function_declaration )
        ( arrow_function )
      ] @node
    ]
    """.strip()
_block_query = """
        (statement_block) @node
    """.strip()

_javascript_exts = [".js", ".ts"]
_jsx_exts = [".jsx", ".tsx"]


class JavascriptClassStrategy(TreeSitterStrategy):
    def __init__(self):
        super().__init__(_javascript_language, _class_query, _javascript_exts)


class JavascriptFunctionStrategy(TreeSitterStrategy):
    def __init__(self):
        super().__init__(_javascript_language, _function_query, _javascript_exts)


class JavascriptBlockStrategy(TreeSitterStrategy):
    def __init__(self):
        super().__init__(_javascript_language, _block_query, _javascript_exts)


class JsxClassStrategy(TreeSitterStrategy):
    def __init__(self):
        super().__init__(_jsx_language, _class_query, _jsx_exts)


class JsxFunctionStrategy(TreeSitterStrategy):
    def __init__(self):
        super().__init__(_jsx_language, _function_query, _jsx_exts)


class JsxBlockStrategy(TreeSitterStrategy):
    def __init__(self):
        super().__init__(_jsx_language, _block_query, _jsx_exts)
