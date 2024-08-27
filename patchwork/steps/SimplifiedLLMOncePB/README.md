# SimplifiedLLMOncePB Documentation

## patchwork/steps/SimplifiedLLMOncePB/typed.py

### Description

This file defines the data types for inputs required by the `SimplifiedLLMOncePB` class. It uses `TypedDict` to specify the expected structure and configurations of these inputs, which include prompts, model specifications, and API keys.

### Inputs

- `json_schema` (Dict[str, Any]): The JSON schema for the expected prompt response.
- `user_prompt` (str): The user input for the prompt.
- `prompt_value` (Dict[str, Any]): Values to be used for the prompt.
- `system_prompt` (str, optional): An additional system-defined prompt.
- `model` (str): The model to be used.
- `openai_api_key` (str, optional): OpenAI API key.
- `anthropic_api_key` (str, optional): Anthropic API key.
- `patched_api_key` (str, optional): Patched API key.
- `google_api_key` (str, optional): Google API key.

These inputs use `StepTypeConfig` annotations to enforce configuration constraints and ensure that at least one of the API keys is provided.

### Outputs

None (this file defines only input types)

## patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Description

This is an empty initialization file. It serves as the entry point for the `SimplifiedLLMOncePB` package, making it a valid Python package directory.

### Inputs

None

### Outputs

None

## patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Description

This file contains the main logic for the `SimplifiedLLMOncePB` class, which extends the `Step` class and relies on the inputs defined in `typed.py`. It prepares the prompt and utilizes the `SimplifiedLLM` class to generate structured JSON responses using a Language Model (LLM).

### Inputs

- `inputs` (SimplifiedLLMOncePBInputs): A dictionary of inputs as defined in `typed.py`.

### Methods

- `__json_schema_as_suffix(prompt: str)`: Adds a JSON schema to the end of a prompt, ensuring the response adheres to the specified format.
- `run() -> dict`: Executes the LLM with the given inputs, processes the response, and returns the structured output.

### Outputs

- `dict`: The structured response from the LLM, including:
  - `extracted_responses` (dict): The extracted values from the LLM response.
  - `request_tokens` (int): Tokens used for the request.
  - `response_tokens` (int): Tokens used for the response.

### Usage

1. Instantiate the `SimplifiedLLMOncePB` class with the required inputs.
2. Call the `run` method to execute the LLM and process the response.
3. The response will be a dictionary containing the extracted values and token usage metrics.