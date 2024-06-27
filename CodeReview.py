import yaml
from pathlib import Path
from patchwork.step import Step
from patchwork.steps import CreatePRComment, PreparePrompt, ReadPRDiffs, CallLLM, PreparePR, ExtractModelResponse


_DEFAULT_INPUT_FILE = Path(__file__).parent / 'defaults.yml'

class CodeReview(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        initial_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        self.inputs = {**initial_inputs, **inputs}

        # User-assigned input values
        # PreparePrompt_1 inputs
        self.inputs['prompt_id'] = 'diffreview'
        self.inputs['prompt_template_file'] = 'prompt.json'
        # CallLLM_1 inputs
        self.inputs['model'] = 'gpt-3.5-turbo'
        self.inputs['allow_truncated'] = 'false'
        # ExtractModelResponse_1 inputs
        self.inputs['response_partitions'] = '{\n  "summary": [\n    "A. Summary:",\n    ""\n  ],\n  "suggestion": [\n    "B. Suggestion:",\n    "A. Summary:"\n  ]\n}'

    def validate_inputs(self):
        missing_inputs = []
        if 'github_api_key' not in self.inputs:
            missing_inputs.append('github_api_key')
        if 'gitlab_api_key' not in self.inputs:
            missing_inputs.append('gitlab_api_key')
        if 'pr_url' not in self.inputs:
            missing_inputs.append('pr_url')
        if 'scm_url' not in self.inputs:
            missing_inputs.append('scm_url')
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
        if 'modified_code_files' not in self.inputs:
            missing_inputs.append('modified_code_files')
        if 'pr_header' not in self.inputs:
            missing_inputs.append('pr_header')
        if 'pr_comments' not in self.inputs:
            missing_inputs.append('pr_comments')
        if 'pr_url' not in self.inputs:
            missing_inputs.append('pr_url')
        if missing_inputs:
            raise ValueError(f'Missing required inputs: {missing_inputs}. Please add them to the defaults.yml file.')

    def run(self) -> dict:
        self.validate_inputs()
        inputs = self.inputs.copy()
        outputs_ReadPRDiffs_1 = ReadPRDiffs(inputs).run()
        step_inputs = {**inputs, 'prompt_value_file': outputs_ReadPRDiffs_1['prompt_value_file'], 'prompt_values': outputs_ReadPRDiffs_1['prompt_values']}
        outputs_PreparePrompt_1 = PreparePrompt(step_inputs).run()
        step_inputs = {**inputs, 'prompts': outputs_PreparePrompt_1['prompts']}
        outputs_CallLLM_1 = CallLLM(step_inputs).run()
        step_inputs = {**inputs, 'new_code': outputs_CallLLM_1['new_code'], 'openai_responses': outputs_CallLLM_1['openai_responses']}
        outputs_ExtractModelResponse_1 = ExtractModelResponse(step_inputs).run()
        step_inputs = {**inputs, 'modified_code_files': outputs_ExtractModelResponse_1['extracted_responses']}
        outputs_PreparePR_1 = PreparePR(step_inputs).run()
        step_inputs = {**inputs, 'pr_comments': outputs_PreparePR_1['pr_body']}
        outputs_CreatePRComment_1 = CreatePRComment(step_inputs).run()
        final_outputs = inputs
        return final_outputs
