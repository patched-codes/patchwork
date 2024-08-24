# Simplified LLM Once PB

## Inputs
- `json_schema`: A dictionary containing JSON schema.
- `user_prompt`: A user prompt specified as a string.
- `prompt_value`: A dictionary representing prompt values.
- `system_prompt`: An optional system prompt specified as a string.
- `model`: A string representing the model.
- `openai_api_key`: A string representing the OpenAI API key with additional configurations.
- `anthropic_api_key`: A string representing the Anthropic API key with additional configurations.
- `patched_api_key`: A string representing API key with additional configurations, including a custom message.
- `google_api_key`: A string representing the Google API key with additional configurations.

## Outputs
- The `SimplifiedLLMOncePB` class inherits from the `Step` class.
- The `run` method processes the inputs provided and returns a dictionary with extracted responses and token information.
- The input parameters are used to configure and run an instance of the `SimplifiedLLM` class with specific prompt values and settings.