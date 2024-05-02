from typing_extensions import NotRequired, TypedDict


class PreparePRInputs(TypedDict):
    modified_code_files: list["ModifiedCodeFile"]
    pr_header: NotRequired[str]


class PreparePROutputs(TypedDict):
    pr_body: str


class ModifiedCodeFile(TypedDict, total=False):
    path: str
    start_line: int
    end_line: int
