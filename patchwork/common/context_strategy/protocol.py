from abc import ABC

from tree_sitter_languages.core import get_parser, get_language
from typing_extensions import Protocol, Tuple

from patchwork.common.context_strategy.position import Position


class ContextStrategyProtocol(Protocol):
    def get_contexts(self, src: list[str]) -> list[Position]:
        ...

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position | None:
        ...

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        ...


class TreeSitterStrategy(ContextStrategyProtocol):
    def __init__(self, language: str, query: str, exts: list[str]):
        self.language = language
        self.query = query
        self.exts = exts

    def query_src(self, src: list[str]):
        language = get_language(self.language)
        parser = get_parser(self.language)
        tree = parser.parse("".join(src).encode("utf-8-sig"))
        return language.query(self.query).captures(tree.root_node)

    def get_contexts(self, src: list[str]) -> list[Position]:
        query_result = self.query_src(src)

        positions = []
        for node, name in query_result:
            if name != "node":
                continue
            position = Position(
                start=node.start_point[0],
                end=node.end_point[0] + 1,
                start_col=node.start_point[1],
                end_col=node.end_point[1] + 1,
            )
            positions.append(position)

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
                    )
                    break

        return positions

    def get_context_indexes(self, src: list[str], start: int, end: int) -> Position | None:
        for position in self.get_contexts(src):
            if position.start <= start and end <= position.end:
                return position

        return None

    def is_file_supported(self, filename: str, src: list[str]) -> bool:
        return any(filename.endswith(ext) for ext in self.exts) and len(src) > 0
