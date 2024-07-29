from typing_extensions import Annotated, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class ScanDepscanInputs(TypedDict):
    language: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ScanDepscanOutputs(TypedDict):
    sbom_vdr_values: dict
