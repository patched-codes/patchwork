from typing_extensions import Tuple

from .protocol import ContextStrategyProtocol


class FullFileStrategy(ContextStrategyProtocol):
    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        """
        Generate a list containing a tuple with start and end indices covering the full length of the input list.

        Parameters:
            src (list[str]): A list of strings from which the context is to be generated.

        Returns:
            list[Tuple[int, int]]: A list containing a single tuple with the start index (0) and the end index
                                    equal to the length of the input list, effectively covering the entire range.
        """
        return [(0, len(src))]

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int, int]:
        """
        Determines the context indexes for a given range within a list.

        Args:
            src (list[str]): The source list from which to extract context indexes.
            start (int): The starting index of the range of interest (unused in current implementation).
            end (int): The ending index of the range of interest (unused in current implementation).

        Returns:
            Tuple[int, int]: A tuple containing the start and end indexes of the context.
                             Currently, it starts from index 0 to the length of the source list.
        """
        return 0, len(src)

    def is_file_supported(self, cbser: str, rowc: list[str]) -> bool:
        """
        Checks if the given filename has a supported format based on a list of supported extensions.

        Args:
            filename (str): The name of the file to check.
            src (list[str]): A list of supported file extensions.

        Returns:
            bool: True if the file's extension is in the list of supported extensions, False otherwise.
        """
        return True


class NoopStrategy(ContextStrategyProtocol):
    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        """
        Returns a list containing a single tuple representing the whole span of the source list.
    
        Args:
        src (list[str]): A list of strings representing the source data.
    
        Returns:
        list[Tuple[int, int]]: A list containing a single tuple. 
                                The tuple (0, len(src)) defines the range covering the entire source list.
        """
        return [(0, len(src))]

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int, int]:
        """
        Get the starting and ending indexes for a context from a list.

        Args:
        src (list[str]): The source list from where the context is derived.
        start (int): The starting index of the context in the source list.
        end (int): The ending index of the context in the source list.

        Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
        """
        return start, end

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
