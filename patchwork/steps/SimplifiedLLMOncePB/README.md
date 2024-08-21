## Patchwork SimplifiedLLMOncePB

### Inputs:
- The `typed.py` file defines the input configuration for `SimplifiedLLMOncePB`.
- Includes required and optional inputs such as `json_schema`, `prompt_user`, `prompt_value`, `prompt_system`, model-related API keys, and messaging for key-generation instructions.

### Outputs:
- The `SimplifiedLLMOncePB.py` file defines the `SimplifiedLLMOncePB` class that inherits from `Step` and takes inputs of type `SimplifiedLLMOncePBInputs`.
- Provides methods to create JSON schemas and run the Simplified Large Language Model according to the provided inputs.
- Returns the extracted responses from the SimplifiedLLM step.