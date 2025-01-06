from pathlib import Path

import yaml

from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import LLM, PR, CallCode2Prompt, ModifyCode

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "default_prompt.json"


class GenerateCodeUsageExample(Step):
    def __init__(self, inputs):
        super().__init__(inputs)

        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        if final_inputs is None:
            final_inputs = {}

        final_inputs.update(inputs)

        final_inputs["prompt_id"] = "GenerateUsageExample"
        if "folder_path" not in final_inputs.keys():
            final_inputs["folder_path"] = Path.cwd()
        else:
            final_inputs["folder_path"] = Path(final_inputs["folder_path"])

        if "prompt_template_file" not in final_inputs:
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        final_inputs["pr_title"] = f"PatchWork Usage Example generated"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({"prompt_values", "files_to_patch"}), LLM, CallCode2Prompt, ModifyCode, PR
        )
        self.inputs = final_inputs

    def run(self):
        outputs = CallCode2Prompt(self.inputs).run()
        new_file_name = f"usage_example.{self.inputs['test_file_extension']}"
        new_file_path = Path(outputs["uri"]).with_name(new_file_name)
        Path(outputs["uri"]).rename(new_file_path)
        outputs["uri"] = str(new_file_path)
        self.inputs["response_partitions"] = {"patch": ["```", "\n", "```"]}
        self.inputs["files_to_patch"] = self.inputs["prompt_values"] = [outputs]
        outputs = LLM(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ModifyCode(self.inputs).run()
        self.inputs.update(outputs)
        number = len(self.inputs["modified_code_files"])
        self.inputs["pr_header"] = f"This pull request adds usage example."
        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
