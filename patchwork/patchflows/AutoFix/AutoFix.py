import json
from enum import IntEnum
from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.logger import logger
from patchwork.step import Step
from patchwork.steps import (
    LLM,
    PR,
    CallLLM,
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


class Compatibility(IntEnum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    UNKNOWN = 0

    @staticmethod
    def from_str(value: str) -> "Compatibility":
        try:
            return Compatibility[value.upper()]
        except KeyError:
            logger.error(f"Invalid compatibility value: {value}")
            return Compatibility.UNKNOWN


class AutoFix(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            CallLLM,
            CommitChanges,
            CreatePR,
            ExtractCode,
            ExtractModelResponse,
            ModifyCode,
            PreparePR,
            PreparePrompt,
            ScanSemgrep,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        self.n = int(final_inputs.get("n", 1))
        self.compatibility_threshold = Compatibility.from_str(final_inputs["compatibility"])

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
            self.inputs["prompt_values"] = outputs.get("files_to_patch", [])
            outputs = LLM(self.inputs).run()
            self.inputs.update(outputs)

            for extracted_response in self.inputs["extracted_responses"]:
                response_compatibility = Compatibility.from_str(
                    extracted_response.get("compatibility", "UNKNOWN").strip()
                )
                if response_compatibility < self.compatibility_threshold:
                    extracted_response.pop("patch", None)

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

        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
