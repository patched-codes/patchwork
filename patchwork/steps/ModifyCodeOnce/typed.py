from typing_extensions import TypedDict


class __ModifyCodePBRequiredInputs(TypedDict):
    file_path: str
    new_code: str


class ModifyCodeOnceInputs(__ModifyCodePBRequiredInputs, total=False):
    start_line: int
    end_line: int


class ModifyCodeOnceOutputs(TypedDict):
    path: str
    start_line: int
    end_line: int
    diff: str
