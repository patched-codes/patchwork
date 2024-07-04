from typing_extensions import Annotated, Sequence, TypedDict

from patchwork.common.utils.typing import IS_CONFIG, IS_PATH


class ScanSemgrepInputs(TypedDict, total=False):
    sarif_file_path: Annotated[str, IS_CONFIG, IS_PATH]
    sarif_values: dict
    semgrep_extra_args: Annotated[Sequence[str], IS_CONFIG]


class ScanSemgrepOutputs(TypedDict):
    sarif_values: dict
