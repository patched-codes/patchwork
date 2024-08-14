from typing_extensions import TypedDict


class ReadFileInputs(TypedDict):
    file_path: str


class ReadFileOutputs(TypedDict):
    file_content: str
