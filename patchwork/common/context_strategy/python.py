import libcst
from libcst import FunctionDef, IndentedBlock, BaseSuite, SimpleStatementLine, BaseCompoundStatement, Expr, SimpleString, ConcatenatedString
from typing_extensions import Callable, Optional, Sequence

from patchwork.common.context_strategy.position import Position
from .protocol import ContextStrategyProtocol


class _PythonCollector(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self):
        super().__init__()
        self.positions: list[Position] = []

    def _visit(self, node: libcst.CSTNode) -> Position:
        code_range = self.get_metadata(libcst.metadata.WhitespaceInclusivePositionProvider, node)
        position = Position(
            start=code_range.start.line - 1,
            end=code_range.end.line - 1,
            start_col=code_range.start.column - 1,
            end_col=code_range.end.column - 1
        )
        self.positions.append(position)
        return position


class _FunctionCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef) -> Optional[bool]:
        position = self._visit(node)
        docstring_node = self._get_docstring_node(node.body)
        if docstring_node:
            code_range = self.get_metadata(libcst.metadata.WhitespaceInclusivePositionProvider, docstring_node)
            comment_position = Position(
                start=code_range.start.line - 1,
                end=code_range.end.line - 1,
                start_col=code_range.start.column - 1,
                end_col=code_range.end.column - 1
            )
            position.meta_positions["comment"] = comment_position

        return True

    def _get_docstring_node(
            self,
            body: BaseSuite | Sequence[SimpleStatementLine| BaseCompoundStatement]
    ) -> Expr | None:
        """ Copied from FunctionDef::get_docstring() """
        if isinstance(body, Sequence):
            if body:
                expr = body[0]
            else:
                return None
        else:
            expr = body
        while isinstance(expr, (BaseSuite, SimpleStatementLine)):
            if len(expr.body) == 0:
                return None
            expr = expr.body[0]
        if not isinstance(expr, Expr):
            return None
        val = expr.value
        if isinstance(val, (SimpleString, ConcatenatedString)):
            return expr
        else:
            return None


class _BlockCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (libcst.metadata.WhitespaceInclusivePositionProvider,)

    def __init__(self):
        super().__init__()

    def visit_IndentedBlock(self, node: IndentedBlock) -> Optional[bool]:
        self._visit(node)
        return True


class PythonStrategy(ContextStrategyProtocol):
    def __init__(self, visitor_func: Callable[[int, int], _PythonCollector]):
        self.visitor_func = visitor_func

    def get_contexts(self, src: list[str]) -> list[Position]:
        cst = libcst.parse_module("".join(src))
        cst_wrapper = libcst.metadata.MetadataWrapper(cst)
        visitor = self.visitor_func()
        cst_wrapper.visit(visitor)

        return visitor.positions

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position | None:
        for position in self.get_contexts(src):
            if position.start <= start and end <= position.end:
                return position

        return None

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
