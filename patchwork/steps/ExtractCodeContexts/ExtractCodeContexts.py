from __future__ import annotations

import os
from pathlib import Path

from patchwork.common.context_strategy.context_strategies import ContextStrategies
from patchwork.common.context_strategy.position import Position
from patchwork.common.utils.filter_paths import (
    IGNORE_DIRS,
    IGNORE_EXTS_GLOBS,
    IGNORE_FILES_GLOBS,
    PathFilter,
)
from patchwork.common.utils.utils import open_with_chardet
from patchwork.logger import logger
from patchwork.step import Step


def get_source_code_contexts(
    filepath: str,
    source_lines: list[str],
    context_strategies: list[str],
    force_code_contexts: bool,
    allow_overlap_contexts: bool,
) -> list[Position]:
    context_strategies = ContextStrategies.get_context_strategies(*context_strategies)
    context_strategies = [
        strategy for strategy in context_strategies if strategy.is_file_supported(filepath, source_lines)
    ]

    positions = []
    for context_strategy in context_strategies:
        contexts = context_strategy.get_contexts(source_lines)

        logger.debug(f'"{context_strategy.__class__.__name__}" Context Strategy used: {len(contexts)} contexts found')
        positions.extend(contexts)

    positions = sorted(positions, key=lambda x: x.start)

    if force_code_contexts:
        for position in positions:
            comment_position = position.meta_positions.get("comment")
            if comment_position is None:
                continue

            position.start = min(position.start, comment_position.start)
            if position.start == comment_position.start:
                position.start_col = comment_position.start_col
            position.end = max(position.end, comment_position.end)
            if position.end == comment_position.end:
                position.end_col = comment_position.end_col
    else:
        positions = [position for position in positions if position.meta_positions.get("comment") is None]

    if not allow_overlap_contexts:
        del_idxs = []
        for i in range(len(positions) - 1):
            if i in del_idxs:
                continue
            for j in range(i + 1, len(positions)):
                if positions[i].end < positions[j].start:
                    break
                del_idxs.append(j)

        for idx in reversed(del_idxs):
            positions.pop(idx)

    return positions


class ExtractCodeContexts(Step):
    required_keys = {}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.base_path = Path(inputs.get("base_path", os.getcwd()))
        self.context_grouping = inputs.get("context_grouping", "ALL")
        # rethink this, should be one level up and true by default
        self.force_code_contexts = inputs.get("force_code_contexts", False)
        self.allow_overlap_contexts = inputs.get("allow_overlap_contexts", True)
        self.max_depth = int(inputs.get("max_depth", -1))

    def run(self) -> dict:
        extracted_code_contexts = []
        for file_path, src, position in self.get_positions(max_depth=self.max_depth):
            extracted_code_context = dict(
                uri=file_path,
                startLine=position.start,
                endLine=position.end,
                affectedCode="".join(src[position.start : position.end]),
            )
            extracted_code_contexts.append(extracted_code_context)

        return dict(
            files_to_patch=extracted_code_contexts,
        )

    def get_positions(self, max_depth: int):
        ignored_groks = IGNORE_DIRS | IGNORE_EXTS_GLOBS | IGNORE_FILES_GLOBS
        path_filter = PathFilter(base_path=self.base_path, ignored_groks=ignored_groks, max_depth=max_depth)

        files_to_consider = []
        if self.base_path.is_file():
            files_to_consider.append(self.base_path)
        else:
            for root, dirs, files in os.walk(self.base_path):
                possible_depth = path_filter.get_depth_ignored(root)
                if possible_depth is not None:
                    dirs[:] = []  # Prune subdirectories
                    continue

                for file in files:
                    file_path = Path(root) / file
                    if not file_path.is_file():
                        continue

                    possible_grok = path_filter.get_grok_ignored(file_path)
                    if possible_grok is not None:
                        logger.warning(f'Ignoring file: {file_path} because of "{possible_grok}" exclusion filter')
                        continue

                    files_to_consider.append(file_path)

        grouping = getattr(ContextStrategies, self.context_grouping, ContextStrategies.ALL)
        if not isinstance(grouping, list):
            grouping = [grouping]

        for file in files_to_consider:
            try:
                with open_with_chardet(file, "r") as f:
                    src = f.read().splitlines(keepends=True)
            except UnicodeDecodeError:
                logger.debug(f"Failed to read file: {file}")
                continue

            for position in get_source_code_contexts(
                str(file), src, grouping, self.force_code_contexts, self.allow_overlap_contexts
            ):
                yield str(file), src, position
