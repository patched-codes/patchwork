from __future__ import annotations

from patchwork.common.context_strategy.languages import GenericLanguage
from patchwork.common.context_strategy.position import Position
from patchwork.common.context_strategy.protocol import ContextStrategyProtocol


class FullFileStrategy(ContextStrategyProtocol):
    def get_contexts(self, src: list[str]) -> list[Position]:
        """Return a list of Position objects representing the context of the source code.

        Args:
            src (list[str]): The source code as a list of strings.

        Returns:
            list[Position]: A list of Position objects representing the context of the source code.
        """
        return [Position(start=0, end=len(src), start_col=0, end_col=len(src[-1]), language=self.language)]

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position:
        """
        Calculate the context indexes based on the input source list and start/end positions.

        Args:
            src (list[str]): The source list of strings.
            start (int): The starting index.
            end (int): The ending index.

        Returns:
            Position: A Position object containing the calculated context indexes.
        """
        return Position(start=0, end=len(src), start_col=0, end_col=len(src[-1]), language=self.language)

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        """
        Checks if the given filename has a supported format based on a list of supported extensions.

        Args:
            filename (str): The name of the file to check.
            src (list[str]): A list of supported file extensions.

        Returns:
            bool: True if the file's extension is in the list of supported extensions, False otherwise.
        """
        return True

    @property
    def language(self) -> GenericLanguage:
        """
        Retrieve the language for the current context strategy.

        Returns:
            str: The language for the current context strategy.
        """
        return GenericLanguage()


class NoopStrategy(ContextStrategyProtocol):
    def get_contexts(self, src: list[str]) -> list[Position]:
        """
        Get the list of Position objects representing contexts based on the source list provided.

        Args:
        src (list[str]): A list of source strings.

        Returns:
        list[Position]: A list of Position objects representing contexts.
        """
        return []

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position:
        """
        Get the context indexes for source code based on the start and end positions.

        Args:
            src (list[str]): The list of source code lines.
            start (int): The starting position.
            end (int): The ending position.

        Returns:
            Position: The context position with start and end indexes and start_col and end_col values.
        """
        return Position(start=start, end=end, start_col=0, end_col=len(src[end - 1]), language=self.language)

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        """
        Check if the given filename is restricted based on a list of restricted keywords.

        Args:
        filename (str): The name of the file to check.
        src (list[str]): A list of strings representing restricted keywords.

        Returns:
        bool: True if the file is restricted, False otherwise.
        """
        return True

    @property
    def language(self) -> GenericLanguage:
        """
        Retrieve the language for the current context strategy.

        Returns:
            str: The language for the current context strategy.
        """
        return GenericLanguage()
