from pydantic import BaseModel
from typing_extensions import Annotated, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class ScanDepscanInputs(BaseModel):
    language: Optional[Annotated[str, StepTypeConfig(is_config=True)]] = None


class ScanDepscanOutputs(BaseModel):
    sbom_vdr_values: dict
