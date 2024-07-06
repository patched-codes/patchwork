The code consists of three files in the `patchwork/steps/LLM` directory: `LLM.py`, `typed.py`, and `__init__.py`.

### File: `LLM.py`
- Size: 1391 bytes
- Created: 2024-07-06 12:05:46
- Modified: 2024-07-06 12:05:46

#### Inputs
The `LLM` class in this file takes inputs to run its process.

#### Code
- The `LLM` class runs a series of steps involving `PreparePrompt`, `CallLLM`, and `ExtractModelResponse`.
- It checks for missing required keys in the provided inputs and raises an error if any are missing.
- It executes the steps and returns the outputs from each step in a dictionary.

### File: `typed.py`
- Size: 1112 bytes
- Created: 2024-07-06 12:05:46
- Modified: 2024-07-06 12:05:46

#### Inputs
Defines the input types for the LLM process including different required keys and their annotations.

#### Code
- Defines the required input keys and their types (`LLMInputs`).
- Defines the output types (`LLMOutputs`) for the LLM process.

### File: `__init__.py`
- Size: 0 bytes
- Created: 2024-07-06 12:05:46
- Modified: 2024-07-06 12:05:46

#### Code
- Empty file.

The `LLM` module seems to be a part of a broader patchwork system that involves natural language processing tasks utilizing various steps such as preparing prompts, calling language models, and extracting model responses.