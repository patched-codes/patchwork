from typing_extensions import TypedDict


class FileWithPatch(TypedDict):
    file_path: str
    start_line: int
    end_line: int
    patch: str


class ModifyCodePBInputs(TypedDict):
    files_with_patch: FileWithPatch


class ModifyCodePBOutputs(TypedDict):
    path: str
    start_line: int
    end_line: int
