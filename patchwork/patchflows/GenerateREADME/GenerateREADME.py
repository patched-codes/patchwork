from pathlib import Path

import yaml

from patchwork.step import Step
from patchwork.steps import (
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

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = CallCode2Prompt(self.inputs).run()
        self.inputs.update(outputs)
        self.inputs["response_partitions"] = {"patch": []}
        outputs = PreparePrompt(self.inputs).run()
        self.inputs.update(outputs)
        outputs = CallLLM(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ExtractModelResponse(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ModifyCode(self.inputs).run()
        self.inputs.update(outputs)

        number = len(self.inputs["modified_code_files"])
        self.inputs["pr_header"] = f"This pull request from patchwork adds {number} READMEs."
        outputs = CommitChanges(self.inputs).run()
        self.inputs.update(outputs)
        outputs = PreparePR(self.inputs).run()
        self.inputs.update(outputs)
        outputs = CreatePR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
