from __future__ import annotations

from pathlib import Path

from patchwork.step import Step, StepStatus
from patchwork.common.utils.utils import open_with_chardet


def save_file_contents(file_path, content):
    """Utility function to save content to a file while preserving line endings.
    
    Args:
        file_path: Path to the file to write to
        content: Content to write to the file
    """
    # Convert content to bytes preserving the exact bytes of line endings
    content_bytes = content.encode('utf-8')
    with open(file_path, "wb") as file:
        file.write(content_bytes)


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
    file_path: str,
    start_line: int | None,
    end_line: int | None,
    new_code: str,
) -> None:
    """Replaces specified lines in a file with new code while preserving line endings.
    
    Args:
        file_path: Path to file to modify
        start_line: Starting line number (0-based) to replace
        end_line: Ending line number to replace (exclusive)
        new_code: New code to insert
        
    This function carefully preserves the original line endings (CRLF vs LF) of the file.
    """
    path = Path(file_path)
    
    # Read existing file in binary mode if it exists to determine endings
    original_ending = b'\n'  # default to LF
    original_content = b''
    file_exists = path.exists()
    
    if file_exists:
        with open(path, 'rb') as f:
            original_content = f.read()
            if b'\r\n' in original_content:
                original_ending = b'\r\n'  # CRLF
    
    # Prepare new code with the correct line endings
    new_code_lines = new_code.splitlines(keepends=False)
    if len(new_code_lines) > 0:
        # Encode each line and add detected/default ending
        new_code_lines = [line.encode('utf-8') + original_ending for line in new_code_lines]
    
    if file_exists and start_line is not None and end_line is not None:
        # Split existing content preserving original endings
        lines = original_content.split(original_ending)
        if original_content.endswith(original_ending):
            lines = lines[:-1]  # Remove empty line from split if file ends with newline
        lines = [line + original_ending for line in lines]
        
        # Convert new code lines for indentation handling
        new_code_decoded = [line.decode('utf-8') for line in new_code_lines]
        lines_decoded = [line.decode('utf-8') for line in lines]
        
        # Handle indentation
        indented_lines = handle_indent(lines_decoded, new_code_decoded, start_line, end_line)
        
        # Convert back to bytes with correct endings
        new_code_lines = [line.encode('utf-8') for line in indented_lines]
        
        # Replace the lines
        lines[start_line:end_line] = new_code_lines
    else:
        lines = new_code_lines

    # Join and write back in binary mode
    content = b''.join(lines)
    save_file_contents(file_path, content.decode('utf-8'))


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
            uri = code_snippet.get("uri")
            start_line = code_snippet.get("startLine")
            end_line = code_snippet.get("endLine")
            new_code = extracted_response.get("patch")

            if new_code is None:
                continue

            replace_code_in_file(uri, start_line, end_line, new_code)
            modified_code_file = dict(path=uri, start_line=start_line, end_line=end_line, **extracted_response)
            modified_code_files.append(modified_code_file)

        return dict(modified_code_files=modified_code_files)
