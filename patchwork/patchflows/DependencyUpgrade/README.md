# DependencyUpgrade

The DependencyUpgrade patchflow aims to automatically update vulnerable versions of dependencies in your repository to the fixed version. 

## How to run?
 
You can run it as follows:

`patchwork DependencyUpgrade`

by default you will need to provide the `openai_api_key` and the `github_api_key` you can pass them as arguments: 

`patchwork DependencyUpgrade openai_api_key=<Your_API_KEY> github_api_key=<Your_GH_Token>`

## What it does?

The DependencyUpgrade patchflow will first scan your repository using an open-source scanner [dep-scan](https://github.com/owasp-dep-scan/dep-scan). It will then extract the vulnerable libraries information detected by the scan and use them to create a prompt to be sent to `gpt-3.5-turbo` to update your package manager file. You can check the default [prompt template](./dependency_upgrade_prompt.json). The fixed package manager file is then committed to the repository under a new branch and finally a pull request is created for the user to review and merge the changes. 

## Configuration

The following are the default configurations that can be modified by the user to adapt the DependencyUpgrade patchflow to their needs. All the options can be set both via CLI arguments and and the yaml config file.

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

### Upgrade Threshold
You can set the upgrade threshold you want to update the libraries to. The accepted values are 'major', 'minor' or  'patch'.
E.g.
```yaml
upgrade_threshold: minor
```
would only upgrade across minor and patch versions of the library, i.e. an upgrade to another major wouldn't be done.

### Severity
You can also set the severity of the vulnerabilities that you want to upgrade. Severity is derived from the CVSS score and can take values of 'none', 'low', 'medium', 'high', and 'critical'. 
E.g.
```yaml
severity: medium
```
means that all libraries that have medium and above vulnerabilities will be upgraded.

### Analyze Impact
By default we update the libraries to their fixed versions. If the upgrades are across major versions or a lot has changed between the versions of the library updating it may break your application. The `analyze_impact` option can be set to enable an impact analysis of the library upgrades as follows:

```yaml
analyze_impact: true
libraries_api_key: <Your_API_KEY>
```
This will get the diff between the vulnerable and fixed versions of the library and determine the impacted methods. Then, we will analyze your repository to determine if you are using the impacted methods. And, finally we will use this information to prompt an LLM to migrate the code that uses these impacted methods in your repository. The code changes are then committed in a new branch in your repository to be included in the same PR that has the update t the package manager file. We use [libraries.io](https://libraries.io/) as the source of information about libraries. You will need to get a free api key from [them](https://libraries.io/api) and set in the options.

### Manage PRs
In addition, there are options to let you manage the PRs as you like, by setting a `branch_prefix`,  or disabling the creation of new branches with `disable_branch` (commits will be made on the current branch). You can also disable PR creation with `disable_pr` or force push commits to existing PR with `force_pr_creation`.

```yaml
branch_prefix: Auto-Generated-Dependency-Upgrades
disable_branch: false
disable_pr: false
force_pr_creation: false
```

### Prompt template

You can update the default [prompt template](./dependency_upgrade_prompt.json). The basic prompt that upgrades the dependencies is with `"id": "depupgrade"`. Note the use of variables `{{Updates}}` and `{{PackageManagerFile}}`. They are generated by the steps within the DependencyUpgrade patchflow and replaced by the actual values during the execution. The expected output response is complete content of the package manager file with the libraries updated to their fixed versions.

## Examples

Here are some example PRs generated with the DependencyUpgrade patchflow:

- https://github.com/codelion/example-python/pull/32
- https://github.com/codelion/example-java-maven/pull/3
