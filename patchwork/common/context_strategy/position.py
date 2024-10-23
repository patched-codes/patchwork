from __future__ import annotations

from attrs import Factory, define

from patchwork.common.context_strategy.languages import LanguageProtocol


@define
class Position:
    start: int
    end: int
    start_col: int
    end_col: int
    language: LanguageProtocol
    meta_positions: dict[str, "Position"] = Factory(dict)

    # def extract_lines(self, src: list[str]) -> list[str]:
    #     return src[self.start : self.end]
    #
    # def extract_text(self, src: list[str]) -> list[str]:
    #     lines = self.extract_lines(src)
    #     lines[0] = lines[0][self.start_col :]
    #     lines[-1] = lines[-1][: self.end_col]
    #     return lines
    #
    # @contextlib.contextmanager
    # def replace_text(self, src: list[str]) -> list[str]:
    #     container = self.extract_text(src)
    #     yield container
    #     src[self.start] = src[self.start][: self.start_col + 1] + container[0]
    #     src[self.start + 1 : self.end - 2] = container[1:-1]
    #     src[self.end - 1] = src[self.end - 1][self.end_col - 1 :] + container[-1]
    #     return


# @dataclasses.dataclass(slots=True, frozen=True)
# class FileSource:
#     filepath: Path
#     src: list[str]
#
#     @contextlib.contextmanager
#     def replace_text(self, position: Position) -> list[str]:
#         with position.replace_text(self.src) as container:
#             yield container
#         return
#
#     def write(self):
#         self.filepath.write_text("".join(self.src))
