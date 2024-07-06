## Contents of the Code

### Inputs:
- **File Name:** `patchwork/steps/LLM/LLM.py`
- **Description:** Defines a class `LLM` that extends `Step`, with an `__init__` method that checks for required inputs and a `run` method that executes a sequence of steps involving other classes like `PreparePrompt`, `CallLLM`, and `ExtractModelResponse`.

### Outputs:
- **File Name:** `patchwork/steps/LLM/typed.py`
- **Description:** Provides typed input schema for the `LLM` step, including required and optional fields for `LLMInputs`, and the expected output structure through `LLMOutputs`.

### Additional Information:
- **File Name:** `patchwork/steps/LLM/__init__.py`
- **Description:** Blank file with no code content.