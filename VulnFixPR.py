import yaml
from pathlib import Path
from patchwork.step import Step
from patchwork.steps import AutoFix, CodeReview


_DEFAULT_INPUT_FILE = Path(__file__).parent / 'defaults.yml'

class VulnFixPR(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        initial_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        self.inputs = {**initial_inputs, **inputs}

    def validate_inputs(self):
        missing_inputs = []
        if 'sarif_values' not in self.inputs:
            missing_inputs.append('sarif_values')
        if 'modified_code_files' not in self.inputs:
            missing_inputs.append('modified_code_files')
        if 'pr_header' not in self.inputs:
            missing_inputs.append('pr_header')
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
        if 'prompts' not in self.inputs:
            missing_inputs.append('prompts')
        if 'openai_responses' not in self.inputs:
            missing_inputs.append('openai_responses')
        if 'extracted_responses' not in self.inputs:
            missing_inputs.append('extracted_responses')
        if 'files_to_patch' not in self.inputs:
            missing_inputs.append('files_to_patch')
        if 'branch_prefix' not in self.inputs:
            missing_inputs.append('branch_prefix')
        if 'branch_suffix' not in self.inputs:
            missing_inputs.append('branch_suffix')
        if 'modified_code_files' not in self.inputs:
            missing_inputs.append('modified_code_files')
        if 'target_branch' not in self.inputs:
            missing_inputs.append('target_branch')
        if 'github_api_key' not in self.inputs:
            missing_inputs.append('github_api_key')
        if 'gitlab_api_key' not in self.inputs:
            missing_inputs.append('gitlab_api_key')
        if 'scm_url' not in self.inputs:
            missing_inputs.append('scm_url')
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
        if 'prompts' not in self.inputs:
            missing_inputs.append('prompts')
        if 'openai_responses' not in self.inputs:
            missing_inputs.append('openai_responses')
        if 'modified_code_files' not in self.inputs:
            missing_inputs.append('modified_code_files')
        if 'pr_header' not in self.inputs:
            missing_inputs.append('pr_header')
        if 'pr_comments' not in self.inputs:
            missing_inputs.append('pr_comments')
        if missing_inputs:
            raise ValueError(f'Missing required inputs: {missing_inputs}. Please add them to the defaults.yml file.')

    def run(self) -> dict:
        self.validate_inputs()
        inputs = self.inputs.copy()
        # User-assigned inputs for AutoFix_1
        inputs['context_size'] = '1000'
        inputs['vulnerability_limit'] = '10'
        inputs['prompt_template_file'] = 'prompt.json'
        inputs['prompt_id'] = 'fix_prompt'
        inputs['allow_truncated'] = 'false'
        inputs['model'] = 'gpt-3.5-turbo'
        inputs['response_partitions'] = '{\n  "commit_message": [\n    "A. Commit message:",\n    "B. Change summary:"\n  ],\n  "patch_message": [\n    "B. Change summary:",\n    "C. Compatibility Risk:"\n  ],\n  "compatibility": [\n    "C. Compatibility Risk:",\n    "D. Fixed Code:"\n  ],\n  "patch": [\n    "D. Fixed Code:",\n    "```",\n    "\\n",\n    "```"\n  ]\n}'
        inputs['disable_branch'] = 'false'
        inputs['force_branch_creation'] = 'true'
        inputs['force_pr_creation'] = 'true'
        inputs['disable_pr'] = 'false'
        outputs_AutoFix_1 = AutoFix(inputs).run()
        # User-assigned inputs for CodeReview_2
        inputs['prompt_id'] = 'diffreview'
        inputs['prompt_template_file'] = 'prompt.json'
        inputs['model'] = 'gpt-3.5-turbo'
        inputs['allow_truncated'] = 'false'
        inputs['response_partitions'] = '{\n  "summary": [\n    "A. Summary:",\n    ""\n  ],\n  "suggestion": [\n    "B. Suggestion:",\n    "A. Summary:"\n  ]\n}'
        step_inputs = {**inputs, 'pr_url': outputs_AutoFix_1['pr_url']}
        outputs_CodeReview_2 = CodeReview(step_inputs).run()
        final_outputs = inputs
        return final_outputs
