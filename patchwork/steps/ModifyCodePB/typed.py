from typing_extensions import TypedDict


class __ModifyCodePBRequiredInputs(TypedDict):
    file_path: str
    new_code: str


class ModifyCodePBInputs(__ModifyCodePBRequiredInputs, total=False):
    start_line: int
    end_line: int


class ModifyCodePBOutputs(TypedDict):
    path: str
    start_line: int
    end_line: int
