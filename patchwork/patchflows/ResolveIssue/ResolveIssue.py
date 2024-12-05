from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import PR, FixIssue, ReadIssues

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class ResolveIssue(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            ReadIssues,
            FixIssue,
            PR,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text()) or dict()
        final_inputs.update(inputs)

        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        validate_steps_with_inputs(
            {"issue_description"}.union(final_inputs.keys()),
            ReadIssues,
            FixIssue,
            PR,
        )

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = ReadIssues(self.inputs).run()
        self.inputs["issue_description"] = outputs
        outputs = FixIssue(self.inputs).run()
        self.inputs.update(outputs)
        self.inputs["pr_header"] = f'This pull request from patchwork fixes {self.inputs["issue_url"]}.'
        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
