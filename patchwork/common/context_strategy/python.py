import libcst
from libcst import FunctionDef, IndentedBlock
from typing_extensions import Callable, Optional, Tuple

from .protocol import ContextStrategyProtocol


class _PythonCollector(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self):
        super().__init__()
        self.positions: list[tuple[int, int]] = []

    def _visit(self, node: libcst.CSTNode) -> bool | None:
        code_range = self.get_metadata(libcst.metadata.WhitespaceInclusivePositionProvider, node)
        self.positions.append((code_range.start.line, code_range.end.line))
        return True


class _FunctionCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef) -> Optional[bool]:
        return self._visit(node)


class _BlockCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self):
        super().__init__()

    def visit_IndentedBlock(self, node: IndentedBlock) -> Optional[bool]:
        return self._visit(node)


class PythonStrategy(ContextStrategyProtocol):
    def __init__(self, visitor_func: Callable[[int, int], _PythonCollector]):
        self.visitor_func = visitor_func

    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        cst = libcst.parse_module("".join(src))
        cst_wrapper = libcst.metadata.MetadataWrapper(cst)
        visitor = self.visitor_func()
        cst_wrapper.visit(visitor)

        return visitor.positions

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int | None, int | None]:
        for context_start, context_end in self.get_contexts(src):
            if context_start <= start and end <= context_end:
                return context_start - 1, context_end - 1

        return None, None

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
