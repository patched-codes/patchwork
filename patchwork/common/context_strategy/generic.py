from typing_extensions import Tuple

from .protocol import ContextStrategyProtocol


class FullFileStrategy(ContextStrategyProtocol):
    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        return [(0, len(src))]

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int, int]:
        return 0, len(src)

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        return True


class NoopStrategy(ContextStrategyProtocol):
    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        return [(0, len(src))]

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int, int]:
        return start, end

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        return True
