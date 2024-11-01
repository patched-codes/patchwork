import json
from pathlib import Path
import yaml

from patchwork.common.utils.step_typing import validate_steps_with_inputs
from patchwork.step import Step
from patchwork.steps import (
    LLM, 
    ReadFile
)

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "default_prompt.json"

class GenerateUnitTests(Step):
    def __init__(self, inputs):
        super().__init__(inputs)

        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        if final_inputs is None:
            final_inputs = {}
        
        final_inputs.update(inputs)

        final_inputs["prompt_id"] = "GenerateUnitTests"
        if "prompt_template_file" not in final_inputs:
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        validate_steps_with_inputs(
            set(final_inputs.keys()).union({"prompt_values"}), LLM, ReadFile
        )
        self.inputs = final_inputs

    def run(self):
        output = ReadFile(self.inputs).run()
        
        # Update inputs with the prompt values, replacing {{code}}
        self.inputs.update(output)
        self.inputs["prompt_values"] = [{"code": output['file_content']}]
        
        outputs = LLM(self.inputs).run()
        return outputs['openai_responses']
