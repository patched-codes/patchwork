from typing_extensions import Protocol, Tuple


class ContextStrategyProtocol(Protocol):
    def get_contexts(self, src: list[str]) -> list[Tuple[int, int]]:
        ...

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Tuple[int | None, int | None]:
        ...

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        ...
