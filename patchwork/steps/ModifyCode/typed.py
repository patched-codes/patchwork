from typing_extensions import Dict, List, TypedDict


class ModifyCodeInputs(TypedDict):
    files_to_patch: List[Dict]
    extracted_responses: List[Dict[str, str]]


class ModifyCodeOutputs(TypedDict):
    modified_code_files: List["ModifiedCodeFile"]


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
