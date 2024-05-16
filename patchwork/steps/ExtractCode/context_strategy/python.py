import libcst
from libcst import FunctionDef, IndentedBlock
from typing_extensions import Callable, Optional, Tuple

from .protocol import ContextStrategyProtocol


class _PythonCollector(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self, start: int, end: int):
        super().__init__()
        self.start = start
        self.end = end
        self.function_start: int | None = None
        self.function_end: int | None = None

    def _visit(self, node: libcst.CSTNode) -> bool | None:
        code_range = self.get_metadata(libcst.metadata.WhitespaceInclusivePositionProvider, node)
        if self.start < code_range.start.line or self.end > code_range.end.line:
            return None

        if self.function_start is not None and self.function_start > code_range.start.line:
            return None

        if self.function_end is not None and self.function_end < code_range.end.line:
            return None

        self.function_start = code_range.start.line
        self.function_end = code_range.end.line
        return True


class _FunctionCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self, start: int, end: int):
        super().__init__(start, end)

    def visit_FunctionDef(self, node: FunctionDef) -> Optional[bool]:
        return self._visit(node)


class _BlockCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self, start: int, end: int):
        super().__init__(start, end)

    def visit_IndentedBlock(self, node: IndentedBlock) -> Optional[bool]:
        return self._visit(node)


class PythonStrategy(ContextStrategyProtocol):
    def __init__(self, visitor_func: Callable[[int, int], _PythonCollector]):
        self.visitor_func = visitor_func

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int | None, int | None]:
        cst = libcst.parse_module("".join(src))
        cst_wrapper = libcst.metadata.MetadataWrapper(cst)
        visitor = self.visitor_func(start, end)
        cst_wrapper.visit(visitor)

        left_rv = visitor.function_start - 1 if visitor.function_start is not None else None
        right_rv = visitor.function_end - 1 if visitor.function_end is not None else None

        return left_rv, right_rv

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        try:
            libcst.parse_module("".join(src))
        except:
            return False
        return filename.endswith(".py") and len(src) > 0


class PythonFunctionStrategy(PythonStrategy):
    def __init__(self):
        super().__init__(_FunctionCollector)


class PythonBlockStrategy(PythonStrategy):
    def __init__(self):
        super().__init__(_BlockCollector)
