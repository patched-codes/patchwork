from pydantic import BaseModel
from typing_extensions import Annotated, List, Optional

from patchwork.common.utils.step_typing import StepTypeConfig


class ScanSemgrepInputs(BaseModel):
    sarif_file_path: Optional[Annotated[str, StepTypeConfig(is_config=True, is_path=True)]] = None
    sarif_values: Optional[dict] = None
    semgrep_extra_args: Optional[Annotated[List[str], StepTypeConfig(is_config=True)]] = None


class ScanSemgrepOutputs(BaseModel):
    sarif_values: dict
