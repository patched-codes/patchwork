# Documentation: patchwork/steps/SimplifiedLLMOncePB

## File: patchwork/steps/SimplifiedLLMOncePB/typed.py

### Overview

The `typed.py` file defines typed input classes for the `SimplifiedLLMOncePB` step in the Patchwork framework. This step leverages the TypedDict feature to ensure input validation and configuration for prompting a language model (LLM).

### Inputs

- `json_schema`: A JSON schema dictionary used for validation.
- `user_prompt`: A string representing the user prompt.
- `prompt_value`: A dictionary containing the prompt values.

#### Optional Inputs

- `system_prompt`: A string representing the system prompt.
- `model`: The model identifier string.
- `openai_api_key`: Key for OpenAI APIs.
- `anthropic_api_key`: Key for Anthropic APIs.
- `patched_api_key`: Key for a patched API, which requires the user to generate an access token and add it via the command line.
- `google_api_key`: Key for Google APIs.

### Code

```python
from typing_extensions import Annotated, Any, Dict, TypedDict

from patchwork.common.utils.step_typing import StepTypeConfig
from patchwork.steps.CallLLM.CallLLM import TOKEN_URL


class __SimplifiedLLMOncePBInputsRequired(TypedDict):
    json_schema: Annotated[Dict[str, Any], StepTypeConfig(is_config=True)]
    # PreparePromptInputs
    user_prompt: Annotated[str, StepTypeConfig(is_config=True)]
    prompt_value: Dict[str, Any]


class SimplifiedLLMOncePBInputs(__SimplifiedLLMOncePBInputsRequired, total=False):
    system_prompt: Annotated[str, StepTypeConfig(is_config=True)]
    # CallLLMInputs
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

## File: patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Overview

The `SimplifiedLLMOncePB.py` file implements the `SimplifiedLLMOncePB` class inheriting from the `Step` class. It encapsulates logic to prepare a prompt and invoke a language model with the provided inputs.

### How to Use

1. Initialize the class with required inputs.
2. Call the `run` method to execute the language model and retrieve the output.

### Inputs

Same as defined in `typed.py`. These include `json_schema`, `user_prompt`, `prompt_value`, `system_prompt`, and API keys.

### Outputs

Returns a dictionary that includes:
- Extracted responses from the LLM.
- Request tokens.
- Response tokens.

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

## File: patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Overview

The `__init__.py` file signifies that the directory `SimplifiedLLMOncePB` is a Python package. The file is currently empty.

### Code

```python

```