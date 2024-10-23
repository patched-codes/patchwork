from __future__ import annotations

import os
from pathlib import Path

from patchwork.common.context_strategy.languages import PythonLanguage
from patchwork.step import Step
from patchwork.steps.ExtractCodeContexts.ExtractCodeContexts import ExtractCodeContexts


class ExtractCodeMethodForCommentContexts(Step):
    required_keys = {}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.base_path = Path(inputs.get("base_path", os.getcwd()))
        # rethink this, should be one level up and true by default
        self.force_code_contexts = inputs.get("force_code_contexts", False)
        self.allow_overlap_contexts = inputs.get("allow_overlap_contexts", True)
        self.max_depth = int(inputs.get("max_depth", -1))

    def run(self) -> dict:
        positions_gen = ExtractCodeContexts(
            dict(
                base_path=self.base_path,
                context_grouping="FUNCTION",
                force_code_contexts=self.force_code_contexts,
                allow_overlap_contexts=self.allow_overlap_contexts,
            )
        ).get_positions(max_depth=self.max_depth)

        extracted_code_contexts = []
        for file_path, src, position in positions_gen:
            comment_position = position.meta_positions.get("comment")
            if comment_position is not None:
                start_line = comment_position.start
                end_line = comment_position.end
            elif isinstance(position.language, PythonLanguage) and position.meta_positions.get("body") is not None:
                # if the comment is not found in python functions/methods, we will use the body position
                body_position = position.meta_positions.get("body")
                start_line = body_position.start
                end_line = body_position.start
            else:
                start_line = position.start
                end_line = position.start

            extracted_code_context = dict(
                uri=file_path,
                startLine=start_line,
                endLine=end_line,
                affectedCode="".join(src[position.start : position.end]),
                commentFormat=position.language.docstring_format,
            )
            extracted_code_contexts.append(extracted_code_context)

        return dict(
            files_to_patch=extracted_code_contexts,
        )
