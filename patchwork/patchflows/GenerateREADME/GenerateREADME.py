from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import (
    LLM,
    PR,
    CallCode2Prompt,
    CallLLM,
    CommitChanges,
    CreatePR,
    ExtractModelResponse,
    ModifyCode,
    PreparePR,
    PreparePrompt,
)

_DEFAULT_PROMPT_JSON = Path(__file__).parent / "generate_readme_prompt.json"
_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class GenerateREADME(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            CallCode2Prompt,
            CallLLM,
            CommitChanges,
            CreatePR,
            ExtractModelResponse,
            ModifyCode,
            PreparePR,
            PreparePrompt,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        if "branch_prefix" not in final_inputs.keys():
            final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        if "prompt_template_file" not in final_inputs.keys():
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        if "prompt_id" not in final_inputs.keys():
            final_inputs["prompt_id"] = "generateREADME"

        if "folder_path" not in final_inputs.keys():
            final_inputs["folder_path"] = Path.cwd()
        else:
            final_inputs["folder_path"] = Path(final_inputs["folder_path"])

        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({"prompt_values", "files_to_patch"}), CallCode2Prompt, LLM, ModifyCode, PR
        )

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = CallCode2Prompt(self.inputs).run()
        self.inputs["files_to_patch"] = self.inputs["prompt_values"] = [outputs]
        self.inputs["response_partitions"] = {"patch": []}
        outputs = LLM(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ModifyCode(self.inputs).run()
        self.inputs.update(outputs)

        number = len(self.inputs["modified_code_files"])
        self.inputs["pr_header"] = f"This pull request from patchwork adds {number} READMEs."
        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
