from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import AgenticLLM, CallSQL

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class LogAnalysis(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            CallSQL,
            AgenticLLM,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({""}),
            CallSQL,
            AgenticLLM,
        )

        self.inputs = final_inputs

    def run(self) -> dict:
        output = CallSQL(self.inputs).run()
        self.inputs.update(output)
