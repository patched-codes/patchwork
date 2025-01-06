from __future__ import annotations

from pathlib import Path
from typing import Union, List

from patchwork.step import Step, StepStatus


def save_file_contents(file_path: str, content: Union[str, bytes]) -> None:
    """Utility function to save content to a file in binary mode to preserve line endings.
    
    Args:
        file_path: Path to the file to write
        content: Content to write, either as string or bytes. If string, it will be encoded as UTF-8."""
    with open(file_path, "wb") as file:
        # Convert string to bytes if needed
        if isinstance(content, str):
            content = content.encode('utf-8')
        file.write(content)


def handle_indent(src: List[str], target: List[str], start: int, end: int) -> List[str]:
    """Handles indentation of new code to match the original code's indentation level.
    
    Args:
        src: Source lines from the original file
        target: New lines that need to be indented
        start: Start line number in the source file
        end: End line number in the source file
    
    Returns:
        List of strings with proper indentation applied
    
    Note:
        - If target is empty, returns it as is
        - If start equals end, uses start + 1 as end to ensure at least one line
        - Preserves existing indentation characters (spaces or tabs)
    """
    if len(target) < 1:
        return target

    if start == end:
        end = start + 1

    # Find first non-empty line in source and target
    first_src_line = next((line for line in src[start:end] if line.strip() != ""), "")
    src_indent_count = len(first_src_line) - len(first_src_line.lstrip())
    first_target_line = next((line for line in target if line.strip() != ""), "")
    target_indent_count = len(first_target_line) - len(first_target_line.lstrip())
    indent_diff = src_indent_count - target_indent_count

    indent = ""
    if indent_diff > 0:
        # Use the same indentation character as the source (space or tab)
        indent_unit = first_src_line[0]
        indent = indent_unit * indent_diff

    return [indent + line for line in target]


def detect_line_ending(content: bytes) -> bytes:
    """Detect the dominant line ending style in the given bytes content.
    
    Args:
        content: File content in bytes to analyze
        
    Returns:
        The detected line ending as bytes (b'\\r\\n', b'\\n', or b'\\r')
        
    Note:
        - Counts occurrences of different line endings (CRLF, LF, CR)
        - Returns the most common line ending
        - Handles cases where \r\n is treated as one ending, not two
        - Defaults to \\n if no line endings are found"""
    crlf_count = content.count(b'\r\n')
    lf_count = content.count(b'\n') - crlf_count  # Don't count \n that are part of \r\n
    cr_count = content.count(b'\r') - crlf_count  # Don't count \r that are part of \r\n
    
    if crlf_count > max(lf_count, cr_count):
        return b'\r\n'
    elif lf_count > cr_count:
        return b'\n'
    elif cr_count > 0:
        return b'\r'
    return b'\n'  # Default to \n if no line endings found

def replace_code_in_file(
    file_path: str,
    start_line: Union[int, None],
    end_line: Union[int, None],
    new_code: str,
) -> None:
    """Replace specified lines in a file with new code while preserving line endings.

    Args:
        file_path: Path to the file to modify
        start_line: Starting line number for replacement (0-based). If None, writes entire file
        end_line: Ending line number for replacement (0-based). If None, writes entire file
        new_code: New content to insert

    Note:
        - Preserves the original file's line ending style (CRLF, LF, or CR)
        - Handles indentation to match the original code
        - Creates new file if it doesn't exist
        - Uses system default line ending for new files
        - Ensures all lines end with proper line ending
        - Preserves UTF-8 encoding
    """
    path = Path(file_path)
    
    # Convert new_code to use \n for initial splitting
    new_code_lines = new_code.splitlines(keepends=True)
    if len(new_code_lines) > 0 and not new_code_lines[-1].endswith("\n"):
        new_code_lines[-1] += "\n"

    if path.exists() and start_line is not None and end_line is not None:
        """Replaces specified lines in a file with new code."""
        # Read file in binary mode to preserve original line endings
        with open(file_path, 'rb') as f:
            content = f.read()
            
        # Detect original line ending
        line_ending = detect_line_ending(content)
        
        # Decode content for line operations
        text = content.decode('utf-8')
        lines = text.splitlines(keepends=True)
        
        # Handle indentation for new code lines
        lines[start_line:end_line] = handle_indent(lines, new_code_lines, start_line, end_line)
        
        # Join all lines and encode ensuring all line endings match the original
        result = ''.join(lines)
        # Normalize to \n first
        result = result.replace('\r\n', '\n').replace('\r', '\n')
        # Then convert to detected line ending
        if line_ending == b'\r\n':
            result = result.replace('\n', '\r\n')
        elif line_ending == b'\r':
            result = result.replace('\n', '\r')
            
        content = result.encode('utf-8')
    else:
        # For new files, use system default line ending
        content = ''.join(new_code_lines).encode('utf-8')

    # Save the modified contents back to the file
    save_file_contents(file_path, content)


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
