## Code Documentation

### Inputs
- **LLMInputs**:
  - Contains required and optional fields for the LLM step:
    - prompt_template_file
    - prompt_id
    - prompt_value_file
    - prompt_values
    - prompt_file
    - model
    - allow_truncated
    - model_args
    - client_args
    - openai_api_key
    - patched_api_key
    - google_api_key
    - response_partitions

### Outputs
- **LLMOutputs**:
  - Contains the output fields for the LLM step:
    - prompts
    - openai_responses
    - extracted_responses

### Additional Information
- **LLM class in LLM.py**:
  - Inherits from Step class and performs a sequence of steps involving PreparePrompt, CallLLM, and ExtractModelResponse.
  - Validates input data against required keys and raises a ValueError if any are missing.
  - The `run` method orchestrates the execution of the three sub-steps and returns the combined output.
- **typed.py**:
  - Defines the structured input and output types for the LLM step.
- **__init__.py**:
  - Contains no code.