from __future__ import annotations

import os
from pathlib import Path

from patchwork.common.context_strategy.langugues import PythonLanguage
from patchwork.logger import logger
from patchwork.step import Step
from patchwork.steps.ExtractCodeContexts.ExtractCodeContexts import ExtractCodeContexts


class ExtractCodeMethodForCommentContexts(Step):
    required_keys = {}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.base_path = Path(inputs.get("base_path", os.getcwd()))
        # rethink this, should be one level up and true by default
        self.force_code_contexts = inputs.get("force_code_contexts", False)
        self.allow_overlap_contexts = inputs.get("allow_overlap_contexts", True)

    def run(self) -> dict:
        positions_gen = ExtractCodeContexts(
            dict(
                base_path=self.base_path,
                context_grouping="FUNCTION",
                force_code_contexts=self.force_code_contexts,
                allow_overlap_contexts=self.allow_overlap_contexts,
            )
        ).get_positions()

        extracted_code_contexts = []
        for file_path, src, position in positions_gen:
            comment_position = position.meta_positions.get("comment")
            if comment_position is not None:
                start_line = comment_position.start
                end_line = comment_position.end
            else:
                start_line = position.start
                end_line = position.start
                if isinstance(position.language, PythonLanguage):
                    start_line = start_line + 1
                    end_line = end_line + 1

            extracted_code_context = dict(
                uri=file_path,
                startLine=start_line,
                endLine=end_line,
                affectedCode="".join(src[position.start : position.end]),
                commentFormat=position.language.docstring_format,
            )
            extracted_code_contexts.append(extracted_code_context)

        logger.info(f"Run completed {self.__class__.__name__}")

        return dict(
            files_to_patch=extracted_code_contexts,
        )
