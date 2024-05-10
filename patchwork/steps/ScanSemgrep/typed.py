from typing_extensions import NotRequired, Sequence, TypedDict


class ScanSemgrepInputs(TypedDict):
    sarif_file_path: NotRequired[str]
    sarif_values: NotRequired[dict]
    semgrep_extra_args: NotRequired[Sequence[str]]


class ScanSemgrepOutputs(TypedDict):
    sarif_values: dict
