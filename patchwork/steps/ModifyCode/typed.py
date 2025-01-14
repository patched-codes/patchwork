from typing_extensions import Dict, List, TypedDict


class ModifyCodeInputs(TypedDict):
    files_to_patch: List[Dict]
    extracted_responses: List[Dict[str, str]]


class ModifyCodeOutputs(TypedDict):
    modified_code_files: List["ModifiedCodeFile"]


class ModifiedCodeFile(TypedDict, total=False):
    """Represents a file that has been modified by the ModifyCode step.
    
    Attributes:
        path: The path to the modified file
        start_line: The starting line number of the modification (1-based)
        end_line: The ending line number of the modification (1-based)
        diff: A unified diff string showing the changes made to the file.
              Generated using Python's difflib with proper file handling
              and cleanup of temporary files.
    
    Note:
        The diff field is generated securely using temporary files that
        are automatically cleaned up. File paths are properly sanitized
        to prevent potential security issues.
    """
    path: str
    start_line: int
    end_line: int
    diff: str
