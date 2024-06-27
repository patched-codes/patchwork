import yaml
from pathlib import Path
from patchwork.step import Step
from patchwork.steps import PreparePrompt, ExtractCode, ExtractModelResponse, ModifyCode, CreatePR, ScanSemgrep, PreparePR, CallLLM, CommitChanges


_DEFAULT_INPUT_FILE = Path(__file__).parent / 'defaults.yml'

class VulnFix(Step):
    def __init__(self, inputs):
        super().__init__(inputs)
        initial_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        self.inputs = {**initial_inputs, **inputs}

    def validate_inputs(self):
        missing_inputs = []
        if 'prompt_value_file' not in self.inputs:
            missing_inputs.append('prompt_value_file')
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
        if 'files_to_patch' not in self.inputs:
            missing_inputs.append('files_to_patch')
        if 'pr_header' not in self.inputs:
            missing_inputs.append('pr_header')
        if 'branch_prefix' not in self.inputs:
            missing_inputs.append('branch_prefix')
        if 'branch_suffix' not in self.inputs:
            missing_inputs.append('branch_suffix')
        if missing_inputs:
            raise ValueError(f'Missing required inputs: {missing_inputs}. Please add them to the defaults.yml file.')

    def run(self) -> dict:
        self.validate_inputs()
        inputs = self.inputs.copy()
        # User-assigned inputs for ScanSemgrep_1
        outputs_ScanSemgrep_1 = ScanSemgrep(inputs).run()
        # User-assigned inputs for ExtractCode_1
        inputs['context_size'] = '1000'
        inputs['vulnerability_limit'] = '10'
        step_inputs = {**inputs, 'sarif_values': outputs_ScanSemgrep_1['sarif_values']}
        outputs_ExtractCode_1 = ExtractCode(step_inputs).run()
        # User-assigned inputs for PreparePrompt_1
        inputs['prompt_template_file'] = 'prompt.json'
        inputs['prompt_id'] = 'fix_prompt'
        step_inputs = {**inputs, 'files_to_patch': outputs_ExtractCode_1['files_to_patch'], 'prompt_values': outputs_ExtractCode_1['prompt_values']}
        outputs_PreparePrompt_1 = PreparePrompt(step_inputs).run()
        # User-assigned inputs for CallLLM_1
        inputs['allow_truncated'] = 'false'
        inputs['model'] = 'gpt-3.5-turbo'
        step_inputs = {**inputs, 'prompts': outputs_PreparePrompt_1['prompts']}
        outputs_CallLLM_1 = CallLLM(step_inputs).run()
        # User-assigned inputs for ExtractModelResponse_1
        inputs['response_partitions'] = '{\n  "commit_message": [\n    "A. Commit message:",\n    "B. Change summary:"\n  ],\n  "patch_message": [\n    "B. Change summary:",\n    "C. Compatibility Risk:"\n  ],\n  "compatibility": [\n    "C. Compatibility Risk:",\n    "D. Fixed Code:"\n  ],\n  "patch": [\n    "D. Fixed Code:",\n    "```",\n    "\\n",\n    "```"\n  ]\n}'
        step_inputs = {**inputs, 'new_code': outputs_CallLLM_1['new_code'], 'openai_responses': outputs_CallLLM_1['openai_responses']}
        outputs_ExtractModelResponse_1 = ExtractModelResponse(step_inputs).run()
        # User-assigned inputs for ModifyCode_1
        step_inputs = {**inputs, 'extracted_responses': outputs_ExtractModelResponse_1['extracted_responses']}
        outputs_ModifyCode_1 = ModifyCode(step_inputs).run()
        # User-assigned inputs for PreparePR_1
        step_inputs = {**inputs, 'modified_code_files': outputs_ModifyCode_1['modified_code_files']}
        outputs_PreparePR_1 = PreparePR(step_inputs).run()
        # User-assigned inputs for CommitChanges_1
        inputs['disable_branch'] = 'false'
        inputs['force_branch_creation'] = 'true'
        step_inputs = {**inputs, 'modified_code_files': outputs_ModifyCode_1['modified_code_files']}
        outputs_CommitChanges_1 = CommitChanges(step_inputs).run()
        # User-assigned inputs for CreatePR_1
        inputs['force_pr_creation'] = 'true'
        inputs['disable_pr'] = 'false'
        step_inputs = {**inputs, 'base_branch': outputs_CommitChanges_1['base_branch'], 'target_branch': outputs_CommitChanges_1['target_branch'], 'pr_body': outputs_PreparePR_1['pr_body']}
        outputs_CreatePR_1 = CreatePR(step_inputs).run()
        final_outputs = {**inputs, 'pr_url': outputs_CreatePR_1['pr_url']}
        return final_outputs
