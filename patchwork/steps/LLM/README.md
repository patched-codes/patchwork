## Inputs
- The `LLM` class requires specific input data defined in `LLMInputs`.
- The required keys for input data are checked in the initialization of the `LLM` class.
- The input data includes information for `PreparePrompt`, `CallLLM`, and `ExtractModelResponse` steps.

## Outputs
- The `run` method of the `LLM` class is responsible for orchestrating the execution of `PreparePrompt`, `CallLLM`, and `ExtractModelResponse` steps.
- The output of the `LLM` class is a dictionary containing the prompts, openai_responses, and extracted_responses obtained from the executed steps.
- The output data format is defined in `LLMOutputs` which is a TypedDict specifying the types of the outputs for each step.