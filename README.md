<div align="center">
  <picture>
    <img alt="Patchwork logo" src="https://repository-images.githubusercontent.com/782544882/a9743f35-5e1c-43ed-a0e0-536322056d38" width="36%">
  </picture>
</div>

<br>

<div align="center">

[![Build Status](https://img.shields.io/github/actions/workflow/status/patched-codes/patchwork/release.yml?logo=github)]()
[![Downloads](https://static.pepy.tech/badge/patchwork-cli)](https://pepy.tech/project/patchwork-cli)
[![Discord](https://img.shields.io/discord/1236886480471855104?style=flat&logo=discord&logoColor=white&label=discord)](https://discord.gg/FVcSNW6v)

[Demo](https://youtu.be/3gRpqQoIino) |
[Docs](https://docs.patched.codes/)

</div>


# PatchWork

An open-source framework for automating development chores using large language models. PatchWork allows you to automate workflows like PR reviews, bug fixing, security patching, and more using a self-hosted CLI agent and your preferred LLMs.

## Key Components

- **Steps**: Reusable atomic actions like Create PR, commit changes, call an LLM etc
- **Prompt Templates**: Customizable LLM prompts optimized for a chore like library updates, code generation, issue analysis etc.
- **Patchflows**: LLM-assisted automations such as PR reviews, code fixing, documentation etc. built by combining steps and prompts.

Patchflows can be run locally in your CLI and IDE, or as part of your CI/CD pipeline. There are [5 patchflows available][] out of the box, and you can always [create your own][].

## Quickstart

<iframe width="560" height="315" src="https://www.youtube.com/embed/3gRpqQoIino?si=9uob9IIHcB04geBY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Installation

### Using Pip

PatchWork is available on PyPI and can be installed using pip:

```bash
pip install patchwork-cli --upgrade
```

### Using Poetry

If you'd like to build from source using poetry, please see detailed documentation `here`[file](INSTALL.md) .

## PatchWork CLI

The CLI runs Patchflows, as follows:

```
patchwork <PatchFlow> <?Arguments>
```

Where
- **Arguments**: Allow for overriding default/optional attributes of the Patchflow in the format of `key=value`. If `key` does not have any value, it is considered a boolean `True` flag.

### Example

For an AutoFix patchflow which patches vulnerabilities based on a scan using Semgrep:

```bash
patchwork AutoFix openai_api_key=<YOUR_OPENAI_API_KEY> github_api_key=<YOUR_GITHUB_TOKEN>
```

The above command will default to patching code in the current directory, by running Semgrep to identify the vulnerabilities. You can take a look at the `default.yml` [file](patchwork/patchflows/AutoFix/defaults.yml) for the list of configurations you can set to manage the AutoFix patchflow. 

You can replace the OpenAI key with a key from our managed service
by signing in at [https://app.patched.codes/signin](https://app.patched.codes/signin) and generating an API key from the integrations tab. You can then call the patchflow with the key as follows:

```bash
patchwork AutoFix patched_api_key=<YOUR_PATCHED_API_KEY> github_api_key=<YOUR_GITHUB_TOKEN>
```

The [patchwork template](https://github.com/patched-codes/patchwork-configs) repository contains the default configuration and prompts for all the patchflows. You can clone that repo and pass it as a flag to the CLI:

```bash
patchwork AutoFix --config /path/to/patchwork-configs/patchflows
```

## Patchflows

Patchwork comes with a set of predefined patchflows, and more will be added over time. Below is a sample list of patchflows:

- AutoFix: Generate and apply fixes to code vulnerabilities in a repository.
- PRReview: On PR creation, extract code diff, summarize changes, and comment on PR.
- GenerateREADME: Create a README markdown file for a given folder, to add documentation to your repository.
- [Experimental] DependencyUpgrade: Update your dependencies from vulnerable to fixed versions.
- [Experimental] ResolveIssue: Identify the files in your repository that need to be updated to resolve an issue (or bug) and create a PR to fix it.

## Prompt Templates

Prompt templates are used by patchflows and passed as queries to LLMs. Templates contain prompts with placeholder variables enclosed by {{}} which are replaced by the data from the steps or inputs on every run. 

Below is a sample prompt template:

```json
{
  "id": "diffreview_summary",
    "prompts": [
      {
        "role": "user",
        "content": "Summarize the following code change descriptions in 1 paragraph. {{diffreviews}}"
      }
    ]
}
```

Each patchflow comes with an optimized default prompt template. But you can specify your own using the `prompt_template_file=/path/to/prompt/template/file` option. 

## Contributing

Contributions for new patchflows and steps, or even to the core framework are welcome. Please look at open issues for details.

- To create a new patchflow, follow [these instructions](patchwork/patchflows/README.md).
- To create a new step, follow [these instructions](patchwork/steps/README.md).

We also provide chat assitants to help you create new steps and patchflows easily. Fair warning: they suffer from the same limitations as their underlying model.

- [Patchwork Assistant GPT](https://chatgpt.com/g/g-0G4sCAd2y-patchwork-assistant) (requires ChatGPT pro subscription)
- [Patchwork Assistant on HuggingChat ](https://hf.co/chat/assistant/66322701fd4787e0c1f7696b) (free)

## Roadmap

### Short Term Q2 '24
- Expand patchflow library and integration options
- Patchflow debugger and validation module
- Bug fixing and performance improvements
- Refactor code and documentation

### Long Term Q3/Q4 '24
- Support large-scale code embeddings in patchflows
- Support parallelization and branching
- Fine-tuned models that can be self-hosted
- Open-source GUI

## License

Patchwork is licensed under [AGPL-3.0 terms](https://github.com/patched-codes/patchwork?tab=AGPL-3.0-1-ov-file#readme). However, custom patchflows and steps can be created and shared using the [patchwork template](https://github.com/patched-codes/patchwork-configs) repository which is licensed under [Apache-2.0 terms](https://github.com/patched-codes/patchwork-configs/blob/main/LICENSE).

