from enum import IntEnum
from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
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
    ScanSonar,
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


class SonarFix(Step):
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
            ScanSonar,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

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

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({"prompt_values"}), ScanSemgrep, ExtractCode, LLM, ModifyCode, PR
        )

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = ScanSonar(self.inputs).run()
        self.inputs.update(outputs)

        self.inputs["prompt_values"] = outputs.get("files_to_patch", [])
        outputs = LLM(self.inputs).run()
        self.inputs.update(outputs)

        for extracted_response in self.inputs["extracted_responses"]:
            response_compatibility = Compatibility.from_str(extracted_response.get("compatibility", "UNKNOWN").strip())
            if response_compatibility < self.compatibility_threshold:
                extracted_response.pop("patch", None)

        outputs = ModifyCode(self.inputs).run()
        self.inputs.update(outputs)

        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
