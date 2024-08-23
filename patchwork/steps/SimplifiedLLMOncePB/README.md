## patchwork/steps/SimplifiedLLMOncePB

### Inputs:
- The code defines a class `SimplifiedLLMOncePBInputs` that stores various input configurations like `user_prompt`, `prompt_value`, `system_prompt`, `model`, `openai_api_key`, `anthropic_api_key`, `patched_api_key`, and `google_api_key`.

### Outputs:
- The main code file `SimplifiedLLMOncePB.py` includes a class `SimplifiedLLMOncePB` that inherits from `Step` and takes `SimplifiedLLMOncePBInputs` as its input class.
- The `SimplifiedLLMOncePB` class has a `run` method that prepares a prompt dictionary based on `user_prompt` and `system_prompt` inputs, then runs an instance of `SimplifiedLLM` with specific configurations and returns the extracted response as a dictionary.