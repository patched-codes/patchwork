## Code Documentation

### Inputs
- **File**: patchwork/steps/LLM/typed.py
  - Contains typed dictionary definitions for input and output data for the LLM step.
  - Defines the structure for required inputs and optional inputs for the LLM step.

### Outputs
- **File**: patchwork/steps/LLM/LLM.py
  - Defines a class named `LLM` that extends the base class `Step`.
  - Constructor validates required input keys and raises an exception if any are missing.
  - The `run` method orchestrates the execution of sub-steps like PreparePrompt, CallLLM, and ExtractModelResponse.
  - Aggregates the outputs from these sub-steps and returns a dictionary of combined results.
  - The returned dictionary includes prompts, OpenAI responses, and extracted responses from the model.