from __future__ import annotations

import libcst
from libcst import (
    BaseCompoundStatement,
    BaseSuite,
    ConcatenatedString,
    Expr,
    FunctionDef,
    IndentedBlock,
    SimpleStatementLine,
    SimpleString,
)
from libcst.metadata import PositionProvider
from typing_extensions import Callable, Optional, Sequence

from patchwork.common.context_strategy.position import Position

from .languages import PythonLanguage
from .protocol import ContextStrategyProtocol


class _PythonCollector(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def __init__(self):
        """
        Initialize a new instance of the class, setting up properties and defaults.
        Inherits from a parent class using super() and initializes an empty list to store positions.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()
        self.positions: list[Position] = []

    def _visit(self, node: libcst.CSTNode) -> Position:
        """
        Visit a CSTNode and record its position within the source code.

        This method leverages the WhitespaceInclusivePositionProvider to obtain
        the start and end positions (lines and columns) of the node, which are then
        adjusted to be zero-indexed. The adjusted position is encapsulated in a
        Position object, added to the `positions` list, and returned.

        Args:
            node (libcst.CSTNode): The CST node whose position is to be determined.

        Returns:
            Position: A Position object representing the zero-indexed start and end
                      line and column numbers of the node within the source code.
        """
        code_range = self.get_metadata(PositionProvider, node)
        position = Position(
            start=code_range.start.line - 1,
            end=code_range.end.line,
            start_col=code_range.start.column - 1,
            end_col=code_range.end.column,
            language=PythonLanguage(),
        )
        self.positions.append(position)
        return position


class _FunctionCollector(_PythonCollector):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def __init__(self):
        """
        Initialize the instance by calling the parent class's constructor.

        Parameters:
        None

        Returns:
        None
        """
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef) -> Optional[bool]:
        """
        Visit a function definition in the AST (Abstract Syntax Tree) and optionally collect
        metadata about its docstring if present.

        Args:
            node (FunctionDef): The AST node for the function definition.

        Returns:
            Optional[bool]: Always returns True indicating successful processing.
        """
        position = self._visit(node)
        docstring_node = self._get_docstring_node(node.body)
        if docstring_node:
            docstring_code_range = self.get_metadata(PositionProvider, docstring_node)
            comment_position = Position(
                start=docstring_code_range.start.line - 1,
                end=docstring_code_range.end.line,
                start_col=docstring_code_range.start.column - 1,
                end_col=docstring_code_range.end.column,
                language=PythonLanguage(),
            )
            position.meta_positions["comment"] = comment_position

        body_code_range = self.get_metadata(PositionProvider, node.body)
        body_position = Position(
            start=body_code_range.start.line - 1,
            end=body_code_range.end.line,
            start_col=body_code_range.start.column - 1,
            end_col=body_code_range.end.column,
            language=PythonLanguage(),
        )
        position.meta_positions["body"] = body_position
        return True

    def _get_docstring_node(
        self, body: BaseSuite | Sequence[SimpleStatementLine | BaseCompoundStatement]
    ) -> Expr | None:
        """
        Copied from FunctionDef::get_docstring()

        This method is used to extract the docstring from the given node.

        Args:
            body (BaseSuite | Sequence[SimpleStatementLine | BaseCompoundStatement]): The body of the node.

        Returns:
            Expr | None: The extracted docstring node or None if not found.
        """
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
    METADATA_DEPENDENCIES = (PositionProvider,)

    def __init__(self):
        """
        Initialize the object by calling the __init__ method of the superclass.
        This method doesn't accept any parameters.
        """
        super().__init__()

    def visit_IndentedBlock(self, node: IndentedBlock) -> Optional[bool]:
        """
        Visit a node of type IndentedBlock and process it using the _visit method.

        Args:
            node (IndentedBlock): The indented block node to visit.

        Returns:
            Optional[bool]: Always returns True after visiting the node.
        """
        self._visit(node)
        return True


class PythonStrategy(ContextStrategyProtocol):
    def __init__(self, visitor_func: Callable[[int, int], _PythonCollector]):
        """
        Initialize the PythonCollector instance.

        Args:
            visitor_func (Callable[[int, int], _PythonCollector]): A function that processes or
                handles two integer values and returns an instance of _PythonCollector.
        """
        self.visitor_func = visitor_func

    def get_contexts(self, src: list[str]) -> list[Position]:
        """
        Extracts and returns positions from a source code.

        Args:
        src (list[str]): A list of strings that represents the source code.

        Returns:
        list[Position]: A list of Position objects representing specific locations within the source code.
        """
        cst = libcst.parse_module("".join(src))
        cst_wrapper = libcst.metadata.MetadataWrapper(cst)
        visitor = self.visitor_func()
        cst_wrapper.visit(visitor)
        return visitor.positions

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position | None:
        """
        Finds the first context in the source list where the specified start and end indices are both
        within the bounds of a context position.

        Parameters:
        src (list[str]): List of strings representing the contexts.
        start (int): The starting index to check within the contexts.
        end (int): The ending index to check within the constraints of the contexts.

        Returns:
        Position | None: Returns the Position object if the start and end indices are contained within any
        context's bounds; otherwise, returns None.
        """
        for position in self.get_contexts(src):
            if position.start <= start and end <= position.end:
                return position
        return None

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        """
        Check if the provided file and source code are supported.

        This method checks if the given source code can be parsed as a Python module and if the
        filename ends with '.py'. Also, it checks if the source code list is not empty.

        Args:
            filename (str): The name of the file to check.
            src (list[str]): A list of strings representing the source code.

        Returns:
            bool: True if the file is supported, False otherwise.
        """
        try:
            libcst.parse_module("".join(src))
        except:
            return False
        return filename.endswith(".py") and len(src) > 0

    @property
    def language(self) -> PythonLanguage:
        return PythonLanguage()


class PythonFunctionStrategy(PythonStrategy):
    def __init__(self):
        """
        Initialize a new instance of the class which automatically
        collects function calls and definitions for processing.

        This method calls the parent class constructor to initialize
        the function collector with the _FunctionCollector class.
        """
        super().__init__(_FunctionCollector)


class PythonBlockStrategy(PythonStrategy):
    def __init__(self):
        """
        Initialize the instance of the class, inheriting properties and methods
        from a parent class with _BlockCollector as an argument to super().
        """
        super().__init__(_BlockCollector)
