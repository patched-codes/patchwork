from __future__ import annotations

from tree_sitter_languages.core import get_language, get_parser
from typing_extensions import Protocol

from patchwork.common.context_strategy.languages import LanguageProtocol
from patchwork.common.context_strategy.position import Position


class ContextStrategyProtocol(Protocol):
    def get_contexts(self, src: list[str]) -> list[Position]:
        """
        Retrieve a list of Positions derived from a given list of source strings.

        Args:
        src (list[str]): A list of source strings from which to derive positions.

        Returns:
        list[Position]: A list of Position objects that have been derived from the source strings.
        """
        ...

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position | None:
        """
        Retrieves the starting and ending indexes of a context within a given source list.

        Args:
            src (list[str]): A list of strings representing the source data.
            start (int): The starting index from where the context should be retrieved.
            end (int): The ending index up to where the context should be retrieved.

        Returns:
            Position | None: Returns a tuple (Position) indicating the start and end indexes.
                             Returns None if the context cannot be extracted based on provided indexes.
        """
        ...

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        """
        Checks if the provided filename is supported by verifying its inclusion in the source list.

        Args:
            filename (str): The name of the file to check.
            src (list[str]): A list of supported filenames.

        Returns:
            bool: True if the file is supported, False otherwise.
        """
        ...

    @property
    def language(self) -> LanguageProtocol:
        """
        Retrieve the language for the current context strategy.

        Returns:
        str: The language for the current context strategy.
        """
        ...


class TreeSitterStrategy(ContextStrategyProtocol):
    def __init__(self, language: str, query: str, exts: list[str], language_protocol: LanguageProtocol):
        """
        Initialize the instance with specified language, query, and file extensions.

        Args:
            language (str): The programming language for the search.
            query (str): The search query.
            exts (list[str]): The list of file extensions to consider for the search.
            language_protocol (LanguageProtocol): The language protocol associated.
        """
        self.tree_sitter_language = language
        self.query = query
        self.exts = exts
        self.language_protocol = language_protocol

    def query_src(self, src: list[str]):
        """
        Execute a syntax query over a given source code list based on the predefined language.

        Args:
        src (list[str]): A list of strings representing the source code to be parsed and queried.

        Returns:
        list: Returns a list of captures that match the query in the source code's abstract syntax tree (AST).
        """
        language = get_language(self.tree_sitter_language)
        parser = get_parser(self.tree_sitter_language)
        tree = parser.parse("".join(src).encode())
        return language.query(self.query).captures(tree.root_node)

    def get_contexts(self, src: list[str]) -> list[Position]:
        """
        Extracts positions of specific nodes from source based on their marking in query results.

        Args:
            src (list[str]): A list of strings representing the source code.

        Returns:
            list[Position]: A list of Position objects that encapsulate the start and end points
                            in the source code for nodes of interest.
        """
        query_result = self.query_src(src)

        positions = []
        # First pass: locate the main "node" elements and store their positions
        for node, name in query_result:
            if name != "node":
                continue
            position = Position(
                start=node.start_point[0],
                end=node.end_point[0] + 1,
                start_col=node.start_point[1],
                end_col=node.end_point[1] + 1,
                language=self.language,
            )
            positions.append(position)

        # Second pass: Locate associated meta nodes and assign to previous positions
        for node, name in query_result:
            if name == "node":
                continue

            for position in positions:
                if node.end_point[0] == position.start - 1:
                    position.meta_positions[name] = Position(
                        start=node.start_point[0],
                        end=node.end_point[0] + 1,
                        start_col=node.start_point[1],
                        end_col=node.end_point[1] + 1,
                        language=self.language,
                    )
                    break

        return positions

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position | None:
        """
        Retrieve position context from a list of strings between specified start and end indices.

        Args:
            src (list[str]): The source list of strings.
            start (int): The starting index to search for the context.
            end (int): The end index to search for the context.

        Returns:
            Position | None: Returns the Position object if found, otherwise returns None if no suitable context is found.
        """
        for position in self.get_contexts(src):
            if position.start <= start and end <= position.end:
                return position

        return None

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        """
        Check if a file is supported based on its extension and ensures the source is not empty.

        Args:
        filename (str): The name of the file to check.
        src (list[str]): The list of source files being checked.

        Returns:
        bool: True if the file's extension is in the list of supported extensions and `src` is not empty, otherwise False.
        """
        return any(filename.endswith(ext) for ext in self.exts) and len(src) > 0

    @property
    def language(self) -> LanguageProtocol:
        return self.language_protocol
