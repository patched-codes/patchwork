from __future__ import annotations

from pathlib import Path

from patchwork.step import Step, StepStatus


def normalize_line_endings(content: str, target_ending: str) -> str:
    """Normalize all line endings in content to the target ending.
    
    Rules:
    1. Normalize any existing line endings to the target ending
    2. Preserve intentional lack of line endings:
       - If original content had no line endings, don't add them
       - If original content had line endings, ensure they're present
    3. Handle mixed line endings by converting all to the target
    """
    # Detect if original content had any line endings
    had_line_endings = ('\r\n' in content) or ('\n' in content) or ('\r' in content)
    ends_with_line_ending = content.endswith('\r\n') or content.endswith('\n') or content.endswith('\r')

    # First standardize all line endings to \n
    tmp = content.replace('\r\n', '\n')  # Convert CRLF to LF
    tmp = tmp.replace('\r', '\n')        # Convert CR to LF
    
    # Then convert all \n to target ending (if not already \n)
    if target_ending != '\n':
        tmp = tmp.replace('\n', target_ending)
    
    # Handle final line ending
    if had_line_endings:
        # If original had line endings, ensure all lines have them
        if not tmp.endswith(target_ending):
            tmp += target_ending
    else:
        # If original had no line endings, remove any we might have added
        if tmp.endswith(target_ending):
            tmp = tmp[:-len(target_ending)]
    
    return tmp

def save_file_contents(file_path, content):
    """Utility function to save content to a file while preserving line endings."""
    # Detect the target line ending from existing file if it exists
    target_ending = '\n'
    if Path(file_path).exists():
        try:
            with open(file_path, 'rb') as f:
                target_ending = detect_line_ending(f.read())
        except Exception:
            pass

    # Normalize line endings in content
    content = normalize_line_endings(content, target_ending)
    
    try:
        # Try UTF-8 first
        content_bytes = content.encode('utf-8')
        with open(file_path, "wb") as file:
            file.write(content_bytes)
    except UnicodeEncodeError:
        # Fallback to system default encoding if UTF-8 fails
        with open(file_path, "w", newline='') as file:
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


def detect_line_ending(content: bytes) -> str:
    """Detect the dominant line ending in a file.
    
    Rules:
    1. If the file has line endings, use the most common one (with CRLF taking precedence if tied)
    2. If the file has no line endings:
       - For empty files or files with no line endings, return '\n' (Unix style)
       - The caller will handle whether to add line endings or not
    """
    if not content:
        return '\n'  # default for empty files
        
    # Count all occurrences first
    crlf_count = content.count(b'\r\n')
    total_lf = content.count(b'\n')
    total_cr = content.count(b'\r')
    
    # Calculate individual counts
    lf_count = total_lf - crlf_count  # Lone \n
    cr_count = total_cr - crlf_count  # Lone \r
    
    # If there are no line endings at all, default to Unix style
    if crlf_count == 0 and lf_count == 0 and cr_count == 0:
        return '\n'
    
    # Return dominant ending with slight bias towards CRLF if it exists
    if crlf_count >= max(lf_count, cr_count):  # Use >= to prefer CRLF when tied
        return '\r\n'
    elif lf_count > cr_count:
        return '\n'
    elif cr_count > 0:
        return '\r'
    return '\n'  # default if no clear winner

def replace_code_in_file(
    file_path: str,
    start_line: int | None,
    end_line: int | None,
    new_code: str,
) -> None:
    path = Path(file_path)
    content = b""
    text = ""
    line_ending = "\n"  # default

    # Read existing file and detect line endings
    if path.exists():
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            line_ending = detect_line_ending(content)
            
            # Try decoding with UTF-8 first, then fallback
            try:
                text = content.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    text = content.decode('latin1')
                except Exception:
                    # If all decodings fail, treat as empty
                    text = ""
        except Exception:
            # If file can't be read, use defaults
            pass

    # Normalize the new code to match the file's line endings
    new_code = normalize_line_endings(new_code, line_ending)
    new_code_lines = new_code.splitlines(keepends=True)

    if path.exists() and start_line is not None and end_line is not None:
        """Replaces specified lines in a file with new code."""
        lines = text.splitlines(keepends=True)

        # Insert the new code at the start line after converting it into a list of lines
        lines[start_line:end_line] = handle_indent(lines, new_code_lines, start_line, end_line)
    else:
        lines = new_code_lines

    # Save the modified contents back to the file
    save_file_contents(file_path, "".join(lines))


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
