from __future__ import annotations

from typing_extensions import Annotated, Any, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig


class __RequiredCallShellInputs(TypedDict):
    script: str


class CallShellInputs(__RequiredCallShellInputs, total=False):
    working_dir: Annotated[str, StepTypeConfig(is_path=True)]
    env: str
    script_template_values: dict[str, Any]


class CallShellOutputs(TypedDict):
    stdout_output: str
