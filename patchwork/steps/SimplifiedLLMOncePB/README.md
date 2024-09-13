# patchwork/steps/SimplifiedLLMOncePB Module Documentation

## Table of Contents
- [patchwork/steps/SimplifiedLLMOncePB/typed.py](#patchworkstepsSimplifiedLLMOncePBtypedpy)
- [patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py](#patchworkstepsSimplifiedLLMOncePBSimplifiedLLMOncePBpy)
- [patchwork/steps/SimplifiedLLMOncePB/__init__.py](#patchworkstepsSimplifiedLLMOncePB__init__py)

---

## patchwork/steps/SimplifiedLLMOncePB/typed.py

### Overview
This file defines the types and input schema required for the `SimplifiedLLMOncePB` step. It uses Python's typing extensions to provide detailed input definitions.

### Inputs:
- `json_schema`: Dictionary following JSON schema format.
- `user_prompt`: String for user input prompt.
- `prompt_value`: Dictionary with values required for the prompt.
- `system_prompt` (Optional): String for system input prompt.
- `model`: String specifying the model name.
- `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key` (Optional): API keys for different services.

### Code:
```python
# Import necessary modules and classes
from typing_extensions import Annotated, Any, Dict, TypedDict
from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.CallLLM.CallLLM import TOKEN_URL

# Define the required inputs
class __SimplifiedLLMOncePBInputsRequired(TypedDict):
    json_schema: Annotated[Dict[str, Any], StepTypeConfig(is_config=True)]
    user_prompt: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_value: Dict[str, Any]

# Define the required and optional inputs
class SimplifiedLLMOncePBInputs(__SimplifiedLLMOncePBInputsRequired, total=False):
    system_prompt: Annotated[str, StepTypeConfig(is_config=True)]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])
    ]
    # Other API keys with similar annotations
    ...
```

---

## patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Overview
This file defines the `SimplifiedLLMOncePB` class, extending the `Step` class and utilizing the input schema from `typed.py`. It runs a simplified Language Learning Model (LLM) step based on provided user and system prompts, and other inputs.

### Inputs:
- The inputs provided in `SimplifiedLLMOncePBInputs` from `typed.py`.

### Outputs:
- A dictionary containing responses with extracted responses and token information from the LLM.

### Usage:
The class can be instantiated and invoked to run an LLM step with simplified inputs.

### Code:
```python
# Import necessary classes
from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOncePB.typed import SimplifiedLLMOncePBInputs

# Define the SimplifiedLLMOncePB class
class SimplifiedLLMOncePB(Step, input_class=SimplifiedLLMOncePBInputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        
        # Store the inputs
        self.user = inputs["user_prompt"]
        self.system = inputs.get("system_prompt")
        self.prompt_value = inputs["prompt_value"]
        self.json_example = inputs["json_schema"]
        self.inputs = inputs

    def run(self) -> dict:
        # Prepare the prompt dictionary
        prompt_dict = {"prompt_user": self.user}
        if self.system:
            prompt_dict["prompt_system"] = self.system

        # Instantiate and run the LLM
        llm = SimplifiedLLM({**self.inputs, **prompt_dict, "prompt_values": [self.prompt_value], "json": True, "json_example": self.json_example})
        llm_output = llm.run()

        # Return response
        return {
            **llm_output.get("extracted_responses")[0],
            "request_tokens": llm_output.get("request_tokens")[0],
            "response_tokens": llm_output.get("response_tokens")[0],
        }
```

---

## patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Overview
This is an empty initialization file for the `SimplifiedLLMOncePB` module.

### Code:
```python

```