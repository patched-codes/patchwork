import os
from pathlib import Path

from patchwork.common.context_strategy.context_strategies import ContextStrategies
from patchwork.common.context_strategy.position import Position
from patchwork.common.ignore import IGNORE_DIRS, IGNORE_EXTS
from patchwork.logger import logger
from patchwork.step import Step


def get_source_code_contexts(
        filepath: str,
        source_lines: list[str],
        context_strategies: list[str],
        force_code_contexts: bool
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

        return positions

    return [position for position in positions if position.meta_positions.get("comment") is None]


class ExtractCodeContexts(Step):
    required_keys = {}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.base_path = Path(inputs.get("base_path", os.getcwd()))
        self.context_grouping = inputs.get("context_grouping", "ALL")
        # rethink this, should be one level up and true by default
        self.force_code_contexts = inputs.get("force_code_contexts", False)

    def run(self) -> dict:
        files_to_consider = []
        for root, dirs, files in os.walk(self.base_path):
            if IGNORE_DIRS.intersection(Path(root).parents):
                continue

            for file in files:
                if any(file.endswith(ext) for ext in IGNORE_EXTS):
                    continue
                files_to_consider.append(self.base_path / file)

        grouping = getattr(ContextStrategies, self.context_grouping, ContextStrategies.ALL)
        if not isinstance(grouping, list):
            grouping = [grouping]

        extracted_code_contexts = []
        for file in files_to_consider:
            src = file.read_text().splitlines(keepends=True)
            for position in get_source_code_contexts(str(file), src, grouping, self.force_code_contexts):
                extracted_code_context = dict(
                    uri=str(file),
                    startLine=position.start,
                    endLine=position.end,
                    affectedCode=''.join(src[position.start : position.end]),
                )
                extracted_code_contexts.append(extracted_code_context)

        logger.info(f"Run completed {self.__class__.__name__}")

        return dict(
            files_to_patch=extracted_code_contexts,
            prompt_values=extracted_code_contexts,
        )
