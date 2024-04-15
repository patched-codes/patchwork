import json
from pathlib import Path

import yaml

from patchwork.step import Step
from patchwork.steps import (
    CallOpenAI,
    CommitChanges,
    CreatePR,
    ExtractCode,
    ExtractModelResponse,
    ModifyCode,
    PreparePR,
    PreparePrompt,
    ScanSemgrep,
)

_DEFAULT_PROMPT_JSON = Path(__file__).parent / "default_prompt.json"
_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class AutoFix(Step):
    def __init__(self, inputs: dict):
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        self.n = int(final_inputs.get("n", 1))
        if "prompt_id" not in final_inputs.keys():
            final_inputs["prompt_id"] = "fixprompt"

        if "prompt_template_file" not in final_inputs.keys():
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        final_inputs["response_partitions"] = {
            "commit_message": ["A. Commit message:", "B. Change summary:"],
            "patch_message": ["B. Change summary:", "C. Compatibility Risk:"],
            "compatibility": ["C. Compatibility Risk:", "D. Fixed Code:"],
            "patch": ["D. Fixed Code:", "```", "\n", "```"],
        }
        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = ScanSemgrep(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ExtractCode(self.inputs).run()
        self.inputs.update(outputs)

        for i in range(self.n):
            outputs = PreparePrompt(self.inputs).run()
            self.inputs.update(outputs)
            outputs = CallOpenAI(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ExtractModelResponse(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ModifyCode(self.inputs).run()
            self.inputs.update(outputs)

            if i == self.n - 1:
                break

            # validation
            self.inputs.pop("sarif_file_path", None)
            outputs = ScanSemgrep(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ExtractCode(self.inputs).run()
            self.inputs.update(outputs)
            if self.inputs.get("prompt_value_file") is not None:
                with open(self.inputs["prompt_value_file"], "r") as fp:
                    vulns = json.load(fp)
                if len(vulns) < 1:
                    break

        outputs = CommitChanges(self.inputs).run()
        self.inputs.update(outputs)
        outputs = PreparePR(self.inputs).run()
        self.inputs.update(outputs)
        outputs = CreatePR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
