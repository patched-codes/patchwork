## Code Documentation

### Inputs

The code defines several input types in the `SimplifiedLLM/typed.py` file:
- `SimplifiedLLMInputsRequired`: Contains `prompt_user` and `prompt_values` variables.
- `SimplifiedLLMInputs`: Extends `SimplifiedLLMInputsRequired` and adds additional variables like `prompt_system`, `model`, `openai_api_key`, etc.

The `SimplifiedLLM` class in `SimplifiedLLM.py` takes these inputs and ensures all required keys are present to create an instance. It then initializes various attributes based on the provided inputs.

### Outputs

The code produces the following outputs:
- `prompts`: List of prompts.
- `openai_responses`: List of responses from OpenAI.
- `extracted_responses`: Extracted responses in a structured format based on the input configurations.

The `run` method in the `SimplifiedLLM` class orchestrates the execution flow, including steps like preparing prompts, calling an LLM model, and extracting responses, generating the final output in a dictionary format.