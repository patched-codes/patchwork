from typing_extensions import TypedDict


class ModifyCodePBInputs(TypedDict):
    file_path: str
    start_line: int
    end_line: int
    new_code: str


class ModifyCodePBOutputs(TypedDict):
    path: str
    start_line: int
    end_line: int
