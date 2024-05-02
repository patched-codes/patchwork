from typing_extensions import NotRequired, TypedDict


class ScanSemgrepInputs(TypedDict):
    sarif_file_path: NotRequired[str]


class ScanSemgrepOutputs(TypedDict):
    sarif_file_path: str
