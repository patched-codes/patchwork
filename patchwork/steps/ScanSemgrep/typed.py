from typing_extensions import Annotated, Sequence, TypedDict

from patchwork.common.utils.types import IS_CONFIG


class ScanSemgrepInputs(TypedDict, total=False):
    sarif_file_path: Annotated[str, IS_CONFIG]
    sarif_values: dict
    semgrep_extra_args: Annotated[Sequence[str], IS_CONFIG]


class ScanSemgrepOutputs(TypedDict):
    sarif_values: dict
