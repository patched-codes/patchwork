## Patchwork SimplifiedLLMOnce

### Inputs
- **_SimplifiedLLMOnceInputsRequired_**
  - prompt_user
  - prompt_value
- **_SimplifiedLLMOnceInputs_**
  - prompt_system
  - model
  - openai_api_key
  - anthropic_api_key
  - patched_api_key
  - google_api_key
  - json
  - response_partitions

### Outputs
- **_SimplifiedLLMOnceOutputs_**
  - prompt
  - openai_response
  - extracted_response

These files are related to a patchwork process for a simplified form of Language Model (LLM) execution. The `typed.py` file defines input and output types. The `SimplifiedLLMOnce.py` file contains the main logic for the process, where prompts are prepared, then sent to an LLM model via `CallLLM`. The response is extracted and returned in a JSON format if requested. The `init.py` file is empty.