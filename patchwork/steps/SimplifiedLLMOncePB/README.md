# Documentation: SimplifiedLLMOncePB Module

## Overview
The `SimplifiedLLMOncePB` module is designed to integrate with large language models (LLMs) by handling the configuration and prompt preparation requirements. It employs the `SimplifiedLLM` class to generate responses based on user and system prompts, and returns a structured output. Below are the details and summaries of the main files in the module.

---

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

- **Extension:** .py
- **Size:** 1616 bytes
- **Created:** 2024-09-02 14:07:45
- **Modified:** 2024-09-02 14:07:45

### Description
This file defines the input types and requirements for the `SimplifiedLLMOncePB` step using `TypedDict` from the `typing_extensions` module.

### Inputs
- **json_schema:** A dictionary schema for JSON validation, marked as required.
- **user_prompt:** A string containing the user's prompt, required for configuring the step.
- **prompt_value:** A dictionary containing values for the prompt, required for configuring the step.
- **system_prompt:** (Optional) A string containing the system prompt.
- **model:** (Optional) A string specifying the model to be used.
- **openai_api_key / anthropic_api_key / patched_api_key / google_api_key:** (Optional) These fields allow for various API keys to be provided for model access.

### Code
```python
from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.CallLLM.CallLLM import TOKEN_URL

class __SimplifiedLLMOncePBInputsRequired(TypedDict):
    json_schema: Annotated[Dict[str, Any], StepTypeConfig(is_config=True)]
    user_prompt: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_value: Dict[str, Any]

class SimplifiedLLMOncePBInputs(__SimplifiedLLMOncePBInputsRequired, total=False):
    system_prompt: Annotated[str, StepTypeConfig(is_config=True)]
    model: Annotated[str, StepTypeConfig(is_config=True)]
    openai_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])
    ]
    patched_api_key: Annotated[
        str,
        StepTypeConfig(
            is_config=True,
            or_op=["openai_api_key", "google_api_key", "anthropic_api_key"],
            msg=f"""\
Model API key not found.
Please login at: "{TOKEN_URL}"
Please go to the Integration's tab and generate an API key.
Please copy the access token that is generated, and add `--patched_api_key=<token>` to the command line.

If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.""",
        ),
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])
    ]
```

---

## File: patchwork/steps/SimplifiedLLMOncePB/__init__.py

- **Extension:** .py
- **Size:** 0 bytes
- **Created:** 2024-09-02 14:07:45
- **Modified:** 2024-09-02 14:07:45

### Description
This is an empty initialization file for the `SimplifiedLLMOncePB` module, designed to recognize the directory as a Python package.

### Code
```python

```

---

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

- **Extension:** .py
- **Size:** 1351 bytes
- **Created:** 2024-09-02 14:07:45
- **Modified:** 2024-09-02 14:07:45

### Description
This file contains the implementation of the `SimplifiedLLMOncePB` class, which orchestrates the creation and execution of prompts for an LLM.

### Inputs
- **inputs:** A dictionary composed of various configurations and prompt-related values supplied by `SimplifiedLLMOncePBInputs`.

### Outputs
- The output is a dictionary containing:
  - **Extracted Responses**
  - **Request Tokens**
  - **Response Tokens**

### Code
```python
from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOncePB.typed import SimplifiedLLMOncePBInputs

class SimplifiedLLMOncePB(Step, input_class=SimplifiedLLMOncePBInputs):
    def __init__(self, inputs):
        super().__init__(inputs)

        self.user = inputs["user_prompt"]
        self.system = inputs.get("system_prompt")
        self.prompt_value = inputs["prompt_value"]
        self.json_example = inputs["json_schema"]
        self.inputs = inputs

    def run(self) -> dict:
        if self.system is not None:
            prompt_dict = dict(
                prompt_system=self.system,
                prompt_user=self.user,
            )
        else:
            prompt_dict = dict(
                prompt_user=self.user,
            )

        llm = SimplifiedLLM(
            {
                **self.inputs,
                **prompt_dict,
                "prompt_values": [self.prompt_value],
                "json": True,
                "json_example": self.json_example,
            }
        )
        llm_output = llm.run()

        return {
            **llm_output.get("extracted_responses")[0],
            "request_tokens": llm_output.get("request_tokens")[0],
            "response_tokens": llm_output.get("response_tokens")[0],
        }
```

---