from __future__ import annotations
from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.typing import IS_CONFIG, IS_PATH


class ScanSemgrepInputs(TypedDict, total=False):
    sarif_file_path: Annotated[str, IS_CONFIG, IS_PATH]
    sarif_values: dict
    semgrep_extra_args: Annotated[list[str], IS_CONFIG]


class ScanSemgrepOutputs(TypedDict):
    sarif_values: dict
