from typing_extensions import Iterable, TypedDict


class ModifyCodeInputs(TypedDict):
    files_to_patch: Iterable[dict]
    extracted_responses: Iterable[dict[str, str]]


class ModifyCodeOutputs(TypedDict):
    modified_code_files: list["ModifiedCodeFile"]


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
