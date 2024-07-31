from typing_extensions import Annotated, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class ScanDepscanInputs(TypedDict, total=False):
    language: Annotated[str, StepTypeConfig(is_config=True)]


class ScanDepscanOutputs(TypedDict):
    sbom_vdr_values: dict
