# Documentation

## Table of Contents
- [SimplifiedLLMOncePB/typed.py](#file-typedpy)
- [SimplifiedLLMOncePB/__init__.py](#file-initpy)
- [SimplifiedLLMOncePB/SimplifiedLLMOncePB.py](#file-simplifiedllmoncepbpy)

## File: SimplifiedLLMOncePB/typed.py

### Overview

This file defines the input types for the `SimplifiedLLMOncePB` class using `TypedDict` and `Annotated` from `typing_extensions`. It specifies the necessary and optional fields that need to be passed to the class for it to function correctly.

### Inputs
- `json_schema`: A JSON schema dictionary used for validation.
- `user_prompt`: A string containing the user's prompt.
- `prompt_value`: A dictionary of values to be used in the prompt.

### Optional Inputs
- `system_prompt`: A string containing the system's prompt.
- `model`: The name of the model to be used.
- `openai_api_key`: OpenAI API key.
- `anthropic_api_key`: Anthropic API key.
- `patched_api_key`: API key handled via a patched method.
- `google_api_key`: Google API key.

### Usage
This is likely used to ensure that all the necessary configurations and data are present and correctly typed before initializing an LLM model-related task.

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

## File: SimplifiedLLMOncePB/__init__.py

### Overview

This file is an empty initializer indicating that `SimplifiedLLMOncePB` is a module. It does not contain any functionality but is necessary for the module's structure.

```python
# Empty file
```

## File: SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Overview

This file defines the `SimplifiedLLMOncePB` class, which extends the `Step` class. It integrates configurations and inputs to prepare and run an LLM with a specified prompt.

### Inputs
- `user_prompt`: User input prompt.
- `system_prompt` (optional): System input prompt.
- `prompt_value`: A dictionary of values to be used in the prompt.
- `json_schema`: A JSON schema dictionary used for validation.
- Model and API keys as defined in `typed.py`.

### Output
- Returns a dictionary with extracted responses and token usage statistics (`request_tokens` and `response_tokens`).

### Usage
To use, instantiate the `SimplifiedLLMOncePB` class with the required inputs and call the `run()` method to get the output.

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