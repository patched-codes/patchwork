# Documentation

## patchwork/steps/SimplifiedLLMOncePB 

### Overview

This module defines the `SimplifiedLLMOncePB` class and its related input types. It integrates a simplified large language model (LLM) interface for once-per-batch processing of prompts.

### Files

- `typed.py`
- `SimplifiedLLMOncePB.py`
- `__init__.py`

---

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

### Description

Defines the input types for the `SimplifiedLLMOncePB` step using `TypedDict` and `Annotated` types from `typing_extensions`.

### Inputs

- `json_schema`: A dictionary representing the JSON schema configuration.
- `user_prompt`: User-defined prompt string.
- `prompt_value`: Dictionary to hold specific values for prompt customization.
- `system_prompt` (optional): System-defined prompt string.
- API keys:
  - `model`: Model identifier.
  - `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`: Various API key annotations with logical `or` operations to ensure at least one is provided.

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

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Description

Provides the `SimplifiedLLMOncePB` class which encapsulates the logic for running a simplified LLM with given inputs. It extends the base `Step` class and uses the `SimplifiedLLMOncePBInputs` for configuration.

### Inputs

- `inputs`: A dictionary consisting of the following keys:
  - `user_prompt`: The main user input prompt.
  - `system_prompt` (optional): A secondary system input prompt.
  - `prompt_value`: A dictionary of specific values to tailor the prompt.
  - `json_schema`: JSON schema definition.
  - Relevant API keys and model information as defined in `SimplifiedLLMOncePBInputs`.

### Outputs

- A dictionary containing:
  - Extracted responses from the LLM.
  - Request and response token information.

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

## File: patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Description

An empty file that is used to indicate that the `SimplifiedLLMOncePB` directory is a module.

### Code
```python

```