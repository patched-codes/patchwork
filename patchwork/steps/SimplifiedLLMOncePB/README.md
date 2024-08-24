# Code Documentation

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

### Inputs
- `json_schema`: JSON schema to provide information about the required inputs.
- `user_prompt`: User prompt for the Simplified LLM model.
- `prompt_value`: Dictionary containing prompt values.
- `system_prompt`: System prompt for the Simplified LLM model.
- `model`: Name of the model to be used.
- `openai_api_key`: API key for OpenAI.
- `anthropic_api_key`: API key for Anthropic.
- `patched_api_key`: Patched API key.
- `google_api_key`: API key for Google.
  
### Outputs
- Definition of the `SimplifiedLLMOncePBInputs` type class with the specified attributes and their configurations.

## File: patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Description
- Empty file, likely providing initialization imports or declarations.

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Description
- Run the Simplified LLM model with the provided inputs.
- Parsing prompts for user and, optionally, system responses.
- Combines prompt values and runs the model.
- Returns the output response along with request/response tokens.

### Inputs
- `user_prompt`: User prompt for the Simplified LLM model.
- `system_prompt`: Optional system prompt for the Simplified LLM model.
- `prompt_value`: Dictionary containing prompt values.
- `json_schema`: JSON schema for input validation.
- Other inputs inherited from `SimplifiedLLMOncePBInputs`.

### Outputs
- A dictionary containing extracted responses, request tokens, and response tokens from the model execution.