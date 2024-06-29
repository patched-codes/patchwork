## Code Documentation

### Inputs
The `LLM` class in `LLM.py` expects inputs conforming to the structure defined in `typed.py` through the `LLMInputs` class. The required input keys are specified in `__LLMInputsRequired` and the optional keys are listed under `LLMInputs`.

### Outputs
The `run` method of the `LLM` class generates outputs in the form of a dictionary containing prompts, openai_responses, and extracted_responses. These outputs are obtained by running a chain of steps: `PreparePrompt`, `CallLLM`, and `ExtractModelResponse`.

### Usage
1. Create an instance of `LLM` by providing the required input data.
2. Execute the `run` method to trigger the processing pipeline that generates and processes prompts, calls out to a language model, and extracts responses.
3. Retrieve the generated outputs from the `run` method for further analysis or usage.