# Summary of Patchwork Code Documentation

## Inputs

### [**patchwork/steps/SimplifiedLLMOncePB/typed.py**](#patchworkstepsSimplifiedLLMOncePBtyped.py)
- Defines the `SimplifiedLLMOncePBInputsRequired` TypedDict for required inputs for SimplifiedLLMOncePB.
- Extends the `SimplifiedLLMOncePBInputs` TypedDict to include optional inputs for SimplifiedLLMOncePB like `system_prompt`, `model`, and various API keys (`openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`).

## Outputs

### [**patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py**](#patchworkstepsSimplifiedLLMOncePBSimplifiedLLMOncePB.py)
- Creates the `SimplifiedLLMOncePB` class that inherits from `Step` and expects inputs of type `SimplifiedLLMOncePBInputs`.
- Defines methods to convert a JSON schema to a prompt suffix and run the SimplifiedLLMOncePB step by utilizing the `SimplifiedLLM` step.

This code seems to be part of a project related to Patchwork and involves running steps for text generation based on specific inputs and prompts.