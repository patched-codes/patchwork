from __future__ import annotations

import difflib
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step, StepStatus


def save_file_contents(file_path: str | Path, content: str) -> None:
    """Utility function to save content to a file.

    Args:
        file_path: Path to the file to save content to (str or Path)
        content: Content to write to the file
    """
    path = Path(file_path)
    with path.open("w") as file:
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


def replace_code_in_file(
    file_path: str | Path,
    start_line: int | None,
    end_line: int | None,
    new_code: str,
) -> None:
    """Replace code in a file at the specified line range.

    Args:
        file_path: Path to the file to modify (str or Path)
        start_line: Starting line number (1-based)
        end_line: Ending line number (1-based)
        new_code: New code to insert
    """
    path = Path(file_path)
    new_code_lines = new_code.splitlines(keepends=True)
    if len(new_code_lines) > 0 and not new_code_lines[-1].endswith("\n"):
        new_code_lines[-1] += "\n"

    if path.exists() and start_line is not None and end_line is not None:
        text = path.read_text()
        lines = text.splitlines(keepends=True)

        # Insert the new code at the start line after converting it into a list of lines
        lines[start_line:end_line] = handle_indent(lines, new_code_lines, start_line, end_line)
    else:
        lines = new_code_lines

    # Save the modified contents back to the file
    save_file_contents(path, "".join(lines))


class ModifyCode(Step):
    UPDATED_SNIPPETS_KEY = "extracted_responses"
    FILES_TO_PATCH = "files_to_patch"
    required_keys = {FILES_TO_PATCH, UPDATED_SNIPPETS_KEY}

    def __init__(self, inputs: dict):
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.files_to_patch = inputs[self.FILES_TO_PATCH]
        self.extracted_responses = inputs[self.UPDATED_SNIPPETS_KEY]

    def run(self) -> dict:
        modified_code_files = []
        sorted_list = sorted(
            zip(self.files_to_patch, self.extracted_responses), key=lambda x: x[0].get("startLine", -1), reverse=True
        )
        if len(sorted_list) == 0:
            self.set_status(StepStatus.SKIPPED, "No code snippets to modify.")
            return dict(modified_code_files=[])

        for code_snippet, extracted_response in sorted_list:
            # Use Path for consistent path handling
            file_path = Path(code_snippet.get("uri", ""))
            start_line = code_snippet.get("startLine")
            end_line = code_snippet.get("endLine")
            new_code = extracted_response.get("patch")

            if new_code is None:
                continue

            # Get the original content for diffing
            diff = ""
            try:
                # Store original content in memory
                original_content = file_path.read_text() if file_path.exists() else ""

                # Apply the changes
                replace_code_in_file(file_path, start_line, end_line, new_code)

                # Read modified content
                current_content = file_path.read_text() if file_path.exists() else ""

                # Generate unified diff
                fromfile = f"a/{file_path}"
                tofile = f"b/{file_path}"
                diff = "".join(
                    difflib.unified_diff(
                        original_content.splitlines(keepends=True),
                        current_content.splitlines(keepends=True),
                        fromfile=fromfile,
                        tofile=tofile,
                    )
                )

                if not diff and new_code:  # If no diff but we have new code (new file)
                    diff = f"+++ {file_path}\n{new_code}"
            except (OSError, IOError) as e:
                logger.warning(f"Failed to generate diff for {file_path}: {str(e)}")
                # Still proceed with the modification even if diff generation fails
                replace_code_in_file(file_path, start_line, end_line, new_code)
                diff = f"+++ {file_path}\n{new_code}"  # Use new code as diff on error

            # Create the modified code file dictionary
            modified_code_file = dict(
                path=str(file_path), start_line=start_line, end_line=end_line, diff=diff, **extracted_response
            )
            modified_code_files.append(modified_code_file)

        return dict(modified_code_files=modified_code_files)
