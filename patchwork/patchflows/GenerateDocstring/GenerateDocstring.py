from pathlib import Path
from typing import Any

import yaml

from patchwork.step import Step
from patchwork.steps import (
    CallLLM,
    CommitChanges,
    CreatePR,
    ExtractModelResponse,
    ModifyCode,
    PreparePR,
    PreparePrompt,
)
from patchwork.steps.ExtractCodeContexts.ExtractCodeContexts import ExtractCodeContexts

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "prompt.json"


class GenerateDocstring(Step):
    def __init__(self, inputs: dict):
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())

        if final_inputs is None:
            final_inputs = {}
        final_inputs.update(inputs)

        if "prompt_template_file" not in final_inputs.keys():
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"
        final_inputs["context_grouping"] = "FUNCTION"
        final_inputs["allow_overlap_contexts"] = False

        self.inputs: dict[str, Any] = final_inputs

    def run(self) -> dict:
        outputs = ExtractCodeContexts(self.inputs).run()
        self.inputs.update(outputs)

        self.inputs["prompt_id"] = "generate_docstring"
        self.inputs["response_partitions"] = {
            "patch": ["Code with docstring:", "```", "\n", "```"],
        }
        outputs = PreparePrompt(self.inputs).run()
        self.inputs.update(outputs)
        outputs = CallLLM(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ExtractModelResponse(self.inputs).run()
        self.inputs.update(outputs)

        # Modify code files with the suggested changes
        outputs = ModifyCode(self.inputs).run()
        self.inputs.update(outputs)

        # Commit changes and create PR
        self.inputs[
            "pr_header"
        ] = f'This pull request from patchwork fixes {len(self.inputs["prompt_values"])} docstrings.'
        outputs = CommitChanges(self.inputs).run()
        self.inputs.update(outputs)
        outputs = PreparePR(self.inputs).run()
        self.inputs.update(outputs)
        outputs = CreatePR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
