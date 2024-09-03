# Documentation

## patchwork/steps/SimplifiedLLMOncePB

This module is designed to create a simplified interface for interacting with a Language Learning Model (LLM), specifically for conducting a single LLM call with the required components defined within a predefined step configuration.

### Files:
1. [typed.py](#file-patchworkstepssimplifiedllmoncepbtypedpy)
2. [\_\_init\_\_.py](#file-patchworkstepssimplifiedllmoncepb__init__py)
3. [SimplifiedLLMOncePB.py](#file-patchworkstepssimplifiedllmoncepbsimplifiedllmoncepbpy)

---

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

- **Extension**: .py
- **Size**: 1616 bytes
- **Created**: 2024-09-03 04:33:20
- **Modified**: 2024-09-03 04:33:20

This file defines the input types required for the SimplifiedLLMOncePB class using `TypedDict` and annotations.

### Inputs:
- `json_schema`: Dict[str, Any] - The JSON schema that specifies the expected data structure.
- `user_prompt`: str - Prompt provided by the user.
- `prompt_value`: Dict[str, Any] - Value of the prompt to be passed to the model.
- Optional `system_prompt`: str - System prompt optionally used alongside the user prompt.
- Optional `model`: str - Name of the LLM model used.
- Multiple possible API keys: `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`.

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

- **Extension**: .py
- **Size**: 0 bytes
- **Created**: 2024-09-03 04:33:20
- **Modified**: 2024-09-03 04:33:20

This file is an empty initialization file used to designate the directory as a Python package.

---

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

- **Extension**: .py
- **Size**: 1351 bytes
- **Created**: 2024-09-03 04:33:20
- **Modified**: 2024-09-03 04:33:20

This file defines the `SimplifiedLLMOncePB` class which extends the `Step` base class. This class handles the execution of the LLM call based on provided inputs and integrates with `SimplifiedLLM`.

### Inputs:
- Inputs are passed as a dictionary containing elements such as `user_prompt`, optional `system_prompt`, and other configurations.

### Outputs:
- A dictionary containing extracted responses and token counts (`request_tokens`, `response_tokens`).

### Code:
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