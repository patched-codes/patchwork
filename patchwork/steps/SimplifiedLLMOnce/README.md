## SimplifiedLLMOnce

### Inputs
- `prompt_user`: User prompt for the model.
- `prompt_value`: Dictionary of prompt values.
- `prompt_system`: System prompt for the model.
- `model`: Selected model.
- `openai_api_key`: OpenAI API key.
- `anthropic_api_key`: Anthropic API key.
- `patched_api_key`: Patched API key.
- `google_api_key`: Google API key.
- `json`: Flag to specify if the response format should be JSON.
- `response_partitions`: Response partitions configuration.

### Outputs
- `prompt`: Generated prompt.
- `openai_response`: Response from the OpenAI model.
- `extracted_response`: Extracted model response in text format.

The code defines data structures for inputs and outputs related to running a simplified version of a Language Model (LLM) once. It defines required and optional inputs, performs the logic to prepare prompts, call the LLM, and extract the model response based on the provided inputs. The `run` method executes the necessary steps and returns the generated prompt, model response, and extracted response.