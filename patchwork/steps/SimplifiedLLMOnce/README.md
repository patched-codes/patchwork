## patchwork/steps/SimplifiedLLMOnce

### Inputs
- `prompt_user`: String content for prompting the user.
- `prompt_value`: Dictionary containing prompt values.
- `prompt_system`: Optional string content for prompting the system.
- `model`: String containing model information.
- `openai_api_key`: String used as the OpenAI API key.
- `anthropic_api_key`: String used as the Anthropic API key.
- `patched_api_key`: String used as a patched API key.
- `google_api_key`: String used as a Google API key.
- `json`: Boolean indicating whether the JSON mode is enabled.
- `response_partitions`: Dictionary containing response partitions.

### Outputs
- `prompt`: Dictionary for the prepared prompt content.
- `openai_response`: String containing the OpenAI response.
- `extracted_response`: Dictionary containing the extracted model response.


This set of code defines input and output types for a SimplifiedLLMOnce step within a patchwork project. The `SimplifiedLLMOnceInputs` class defines the required and optional inputs with type annotations and configuration settings. The `SimplifiedLLMOnceOutputs` class specifies the expected output types. The main `SimplifiedLLMOnce` class is implemented as a step in executing a sequence of related tasks involving preparing a prompt, calling an LLM (large language model), and extracting the model's response. The step logic handles JSON processing, input validation, and task execution.