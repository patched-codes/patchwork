import yaml
from pathlib import Path
from patchwork.step import Step
from patchwork.steps import CallLLM, PreparePrompt, ExtractModelResponse


_DEFAULT_INPUT_FILE = Path(__file__).parent / 'defaults.yml'

class VulnFix(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        initial_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        self.inputs = {**initial_inputs, **inputs}

        # User-assigned input values
        # PreparePrompt_1 inputs
        self.inputs['prompt_id'] = 'fix_prompt'
        # CallLLM_1 inputs
        self.inputs['model'] = 'gpt-3.5-turbo'
        self.inputs['allow_truncated'] = 'false'
        # ExtractModelResponse_1 inputs
        self.inputs['response_partitions'] = '{}'

    def validate_inputs(self):
        missing_inputs = []
        if 'prompt_template_file' not in self.inputs:
            missing_inputs.append('prompt_template_file')
        if 'prompt_value_file' not in self.inputs:
            missing_inputs.append('prompt_value_file')
        if 'prompt_values' not in self.inputs:
            missing_inputs.append('prompt_values')
        if 'client_args' not in self.inputs:
            missing_inputs.append('client_args')
        if 'google_api_key' not in self.inputs:
            missing_inputs.append('google_api_key')
        if 'model_args' not in self.inputs:
            missing_inputs.append('model_args')
        if 'openai_api_key' not in self.inputs:
            missing_inputs.append('openai_api_key')
        if 'patched_api_key' not in self.inputs:
            missing_inputs.append('patched_api_key')
        if 'prompt_file' not in self.inputs:
            missing_inputs.append('prompt_file')
        if missing_inputs:
            raise ValueError(f'Missing required inputs: {missing_inputs}. Please add them to the defaults.yml file.')

    def run(self) -> dict:
        self.validate_inputs()
        inputs = self.inputs.copy()
        outputs_PreparePrompt_1 = PreparePrompt(inputs).run()
        step_inputs = {**inputs, 'prompts': outputs_PreparePrompt_1['prompts']}
        outputs_CallLLM_1 = CallLLM(step_inputs).run()
        step_inputs = {**inputs, 'new_code': outputs_CallLLM_1['new_code'], 'openai_responses': outputs_CallLLM_1['openai_responses']}
        outputs_ExtractModelResponse_1 = ExtractModelResponse(step_inputs).run()
        final_outputs = {**inputs, 'extracted_responses': outputs_ExtractModelResponse_1['extracted_responses']}
        return final_outputs
