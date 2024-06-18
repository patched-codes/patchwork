# GenerateDocstring

The GenerateDocstring patchflow aims to automatically document methods in your code by generating docstrings. 

## How to run?
 
You can run it as follows:

`patchwork GenerateDocstring`

by default you will need to provide the `openai_api_key` and the `github_api_key` you can pass them as arguments: 

`patchwork GenerateDocstring openai_api_key=<Your_API_KEY> github_api_key=<Your_GH_Token>`

## What it does?

The GenerateDocstring patchflow starts from a `base_path` (default is the current directory), recursively traverse the directory to extract methods from the source code files. It will then use them to create a prompt to be sent to `gpt-3.5-turbo` to update the source code with the docstrings. You can check the default [prompt template](./prompt.json). The udpated files are then committed to the repository under a new branch and finally a pull request is created for the user to review and merge the changes. 

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

### Base Path
You can set the base path from where to begin the docstring generation.
E.g.
```yaml
base_path: ./GitHub/example-python/
```

### Rewrite Existing
You can choose if you want to retain the existing docstrings or generate new ones. 
E.g.
```yaml
rewrite_existing: true
```
means that existing docstrings in methods would be replaced by new ones that are generated.

### Manage PRs
In addition, there are options to let you manage the PRs as you like, by setting a `branch_prefix`,  or disabling the creation of new branches with `disable_branch` (commits will be made on the current branch). You can also disable PR creation with `disable_pr` or force push commits to existing PR with `force_pr_creation`.

```yaml
branch_prefix: Auto-Generated-Docstrings
disable_branch: false
disable_pr: false
force_pr_creation: false
```

### Prompt template

You can update the default [prompt template](./prompt.json). The basic prompt that generates the docstrings is with `"id": "generate_docstring"`. Note the use of variable `{{affectedCode}}`. During the GenerateDocstring patchflow the actual value of this variable is filled in during the execution. The expected output response is complete content of the file with the docstrings.

## Examples

Here are some example PRs generated with the GenerateDocstring patchflow:

- https://github.com/codelion/example-python/pull/45
- https://github.com/codelion/example-java-maven/pull/4
