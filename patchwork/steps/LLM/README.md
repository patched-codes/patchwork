# Documentation for LLM Step in Patchwork

## Inputs
The `LLM` class in `LLM.py` defines the required input structure for the LLM (Large Language Model) step named `LLMInputs`. The inputs include various configurations like files, API keys, model settings, and prompt details for tasks like preparing prompts, calling LLM, and extracting responses. The required input keys are specified within the `LLMInputs` structure.

## Outputs
The `run()` method of the `LLM` class in `LLM.py` orchestrates the preparation, calling, and extraction steps by invoking relevant sub-steps (`PreparePrompt`, `CallLLM`, and `ExtractModelResponse`). The method returns a dictionary containing prompts, LLM responses, and extracted responses from the model.

## Additional Information
- The `typed.py` file defines the specific structure of the inputs (`LLMInputs`) and outputs (`LLMOutputs`) for the LLM step, specifying required and optional parameters for each sub-step involved in the process.
- The `__init__.py` file is empty as it only serves as a placeholder within the `LLM` module structure.