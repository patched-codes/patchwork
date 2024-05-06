# AutoFix

The AutoFix patchflow aims to automatically fix code vulnerabilities in your repository. 

## How to run?
 
You can run it as follows:

`patchwork AutoFix`

by default you will need to provide the `openai_api_key` and the `github_api_key` you can pass them as arguments: 

`patchwork AutoFix openai_api_key=<Your_API_KEY> github_api_key=<Your_GH_Token>`

## What it does?

The AutoFix patchflow will first scan the code in your repository using an open-source scanner Semgrep. It will then take the vulnerabilities that are detected by the scan and create a prompt to be sent to `gpt-3.5-turbo` to generate the fix for the vulnerabilities. You can check the default [prompt template](./default_prompt.json). The generated fixes are then committed to the repository under a new branch and finally a pull request is created for the user to review and merge the changes. 

## Configuration

The following are the default configurations that can be modified by the user to adapt the AutoFix patchflow to their needs. All the options can be set both via CLI arguments and and the yaml config file.

### Model

You can choose any LLM API as long as it has an OpenAI API compatible chat completions endpoint. Just update the default values of the following options:

```yaml
- model: gpt-3.5-turbo
- client_base_url: https://api.openai.com/v1
```

E.g. to use Meta's CodeLlama model from HuggingFace you can set:

```yaml
client_base_url: https://api-inference.huggingface.co/models/codellama/CodeLlama-70b-Instruct-hf/v1
model: codellama/CodeLlama-70b-Instruct-hf
model_temperature: 0.2
model_top_p: 0.95
model_max_tokens: 2000
```
and pass your HuggingFace token in the `openai_api_key` option.

You can also use llama.cpp to run inference on CPU locally. Just install the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) package and run their OpenAI compatible web server as described [here](https://github.com/abetlen/llama-cpp-python) with the command:

`python3 -m llama_cpp.server --hf_model_repo_id TheBloke/deepseek-coder-6.7B-instruct-GGUF --model 'deepseek-coder-6.7b-instruct.Q4_K_M.gguf' --chat_format chatml`

Once the local server is running you can set:

```yaml
client_base_url: http://localhost:8000/v1
model: TheBloke/deepseek-coder-6.7B-instruct-GGUF
model_temperature: 0.2
model_top_p: 0.95
model_max_tokens: 1000
```
and use the local model for inference.

### Context size
By default we chunk the code to `context_size` tokens to pass on to the LLM. You can change the default value by setting:

```yaml
context_size: 1000
```
in general we have found that a larger `context_size `doesn't necessarily lead to better fixes.

### Semgrep extra args
You can pass any additional arguments to the Semgrep scanner using the `semgrep_extra_args` option as follows:

```yaml
semgrep_extra_args: --config auto
```

### SARIF input
We can use any SAST scanner that can export the results in SARIF format. Just set the `sarif_file_path` to the SARIF file and AutoFix will use the information there to generate the fixes. Otherwise, we will do a scan using Semgrep.

```yaml
sarif_file_path: /path/to/sarif/file
```

### Vulnerability limit
By default we process and fix only `vulnerability_limit` number of issues. This is to avoid making large number of LLMs calls and to keep the generated PR manageable. You can set the value to your preference:

```yaml
vulnerability_limit: 10
``` 
set this value to a negative number (e.g. `-1`) to fix all vulnerabilities found in the scan.

### Severity
You can also set the severity of the vulnerabilities that you want to fix. Severity is derived from the information available in the SARIF file and can take values of 'unknown', 'note'/'info', 'warning'/'low', 'medium', 'error'/'high', and 'critical'. E.g.

```yaml
severity: medium
```
means that all medium and above vulnerabilities will be fixed.

### Compatibility
You can also set the compatibility threshold of the suggested fixes to be included in the pull request. Compatibility can take values of 'unknown', 'low', 'medium', and 'high'. E.g.

```yaml
compatibility: medium
```
means that all fixes with mediuam and above threshold will be included in the PR.

### Manage PRs
In addition, there are options to let you manage the PRs as you like, by setting a `branch_prefix`,  or disabling the creation of new branches with `disable_branch` (commits will be made on the current branch). You can also disable PR creation with `disable_pr` or force push commits to existing PR with `force_pr_creation`.

```yaml
branch_prefix: Auto-Generated-Fixes
disable_branch: false
disable_pr: false
force_pr_creation: false
```

### Scanner
By default we use the open-source Semgrep scanner that comes with a community rule set for finding vulnerabilities. You can also do a `semgrep login` before running the AutoFix patchflow to get access to your own custom or pro rules if you have a Semgrep account (available for free).  In addition, you can use any SAST scanner that outputs results in the standard SARIF format. Just pass your scan results with the following:

```yaml
sarif_file_path: /path/to/your/sarif.json
```

### Prompt template

You can update the default [prompt template](./default_prompt.json). Note the use of variables `{{messageText}}` and `{{affectedCode}}`. They are generated by the steps within the AutoFix patchflow and replaced by the actual values during the execution. Also, remember to keep the output format as given in the default prompt as it is used to extract information that is used by the steps after the model response is processed.  The following output format is expected at the moment:
```
A. Commit message:
<brief summary of the diff>

B. Change summary:
<description of the changes made in the diff>

C. Compatibility Risk:
<Low, Medium, High> 

D. Fixed Code:
<original code with the vulnerability now fixed>
```

## Examples

Here are some example PRs generated with the AutoFix patchflow:

- https://github.com/patched-codes/AltoroJ/pull/7
- https://github.com/patched-codes/pygoat/pull/2
