from __future__ import annotations

import json
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step


def load_json_file(file_path):
    """Utility function to load a json file."""
    file_path = Path(file_path)

    if not file_path.is_file():
        raise ValueError(f'Unable to find input file: "{file_path}"')
    try:
        with open(file_path, "r") as fp:
            return json.load(fp)
    except json.JSONDecodeError as e:
        raise ValueError(f'Invalid input file "{file_path}": {e}')


def save_file_contents(file_path, content):
    """Utility function to save content to a file."""
    with open(file_path, "w") as file:
        file.write(content)


def handle_indent(src: list[str], target: list[str], start: int, end: int) -> list[str]:
    if len(target) < 1:
        return target

    if start == end:
        end = start + 1

    first_src_line = next((line for line in src[start:end] if line.strip() != ""), "")
    src_indent_count = len(first_src_line) - len(first_src_line.lstrip())
    first_target_line = next((line for line in target if line.strip() != ""), "")
    target_indent_count = len(first_target_line) - len(first_target_line.lstrip())
    indent_diff = src_indent_count - target_indent_count

    indent = ""
    if indent_diff > 0:
        indent_unit = first_src_line[0]
        indent = indent_unit * indent_diff

    return [indent + line for line in target]


def replace_code_in_file(file_path, start_line, end_line, new_code):
    """Replaces specified lines in a file with new code."""
    with open(file_path, "r") as file:
        text = file.read()

    lines = text.splitlines(keepends=True)

    # Insert the new code at the start line after converting it into a list of lines
    lines[start_line:end_line] = handle_indent(lines, new_code.splitlines(keepends=True), start_line, end_line)

    # Save the modified contents back to the file
    save_file_contents(file_path, "".join(lines))


class ModifyCode(Step):
    UPDATED_SNIPPETS_KEY = "extracted_responses"
    FILES_TO_PATCH = "files_to_patch"
    required_keys = {FILES_TO_PATCH, UPDATED_SNIPPETS_KEY}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.files_to_patch = inputs[self.FILES_TO_PATCH]
        self.extracted_responses = inputs[self.UPDATED_SNIPPETS_KEY]

    def run(self) -> dict:
        modified_code_files = []
        sorted_list = sorted(
            zip(self.files_to_patch, self.extracted_responses), key=lambda x: x[0]["startLine"], reverse=True
        )
        for code_snippet, extracted_response in sorted_list:
            uri = code_snippet["uri"]
            start_line = code_snippet["startLine"]
            end_line = code_snippet["endLine"]
            new_code = extracted_response.get("patch")
            if new_code is None:
                continue

            replace_code_in_file(uri, start_line, end_line, new_code)
            modified_code_file = dict(path=uri, start_line=start_line, end_line=end_line, **extracted_response)
            modified_code_files.append(modified_code_file)

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(modified_code_files=modified_code_files)
