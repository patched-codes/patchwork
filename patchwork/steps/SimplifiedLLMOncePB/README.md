# Documentations for `patchwork/steps/SimplifiedLLMOncePB`

## Overview

This directory contains three Python files which form part of a larger AI project framework. These files define data structures and classes central to interacting with Long Language Models (LLMs) using simplified prompts.

## File: `patchwork/steps/SimplifiedLLMOncePB/typed.py`

### Description
This file contains type definitions for the inputs required by the `SimplifiedLLMOncePB` class. The structure used is based on Python's `TypedDict` from the `typing_extensions` module, which allows defining a dictionary with a fixed set of keys and associated types.

### Inputs

- `json_schema`: A dictionary defining the JSON schema to be used, wrapped with the `StepTypeConfig`.
- `user_prompt`: A string representing the user's prompt, also wrapped in `StepTypeConfig`.
- `prompt_value`: A dictionary containing prompt values.
- `system_prompt` (optional): A string for the system prompt, if provided.
- `model`: A string representing the model to be used.
- `openai_api_key`: An API key for OpenAI services.
- `anthropic_api_key`: An API key for Anthropic services.
- `patched_api_key`: A general-purpose API key for the system, if specific keys are not provided.
- `google_api_key`: API key for Google services.

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
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])]
    anthropic_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["openai_api_key", "google_api_key", "anthropic_api_key"], msg=f"""\
Model API key not found.
Please login at: "{TOKEN_URL}"
Please go to the Integration's tab and generate an API key.
Please copy the access token that is generated, and add `--patched_api_key=<token>` to the command line.

If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.""")]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])]
```

## File: `patchwork/steps/SimplifiedLLMOncePB/__init__.py`

### Description
This is an empty file that typically serves to mark the directory as a Python package directory. It does not contain any executable code.

### Code
```python

```

## File: `patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py`

### Description
This file defines the `SimplifiedLLMOncePB` class, a subclass of `Step`. It is used to encapsulate the logic required for running a prompt through an LLM in a simplified manner. The class takes various inputs, merges them into a cohesive prompt, and returns parsed JSON results.

### Inputs
The `SimplifiedLLMOncePB` class uses the `SimplifiedLLMOncePBInputs` type definitions from `typed.py`.

### Outputs
The `run` method returns a dictionary containing:
- Processed responses from the LLM.
- Metadata about the request and response tokens.

### Code
```python
import json

from patchwork.step import Step
from patchwork.steps.SimplifiedLLM.SimplifiedLLM import SimplifiedLLM
from patchwork.steps.SimplifiedLLMOncePB.typed import SimplifiedLLMOncePBInputs

class SimplifiedLLMOncePB(Step, input_class=SimplifiedLLMOncePBInputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.user = inputs["user_prompt"]
        self.system = inputs.get("system_prompt")
        self.prompt_value = inputs["prompt_value"]
        self.json_schema = inputs["json_schema"]
        self.inputs = inputs

    def __json_schema_as_suffix(self, prompt: str):
        return f"""\
{prompt}
Respond only with the following json format, do not include any additional information:
{json.dumps(self.json_schema)}
"""

    def run(self) -> dict:
        if self.system is not None:
            prompt_dict = dict(
                prompt_system=self.__json_schema_as_suffix(self.system),
                prompt_user=self.user,
            )
        else:
            prompt_dict = dict(
                prompt_user=self.__json_schema_as_suffix(self.user),
            )

        llm = SimplifiedLLM(
            {
                **self.inputs,
                **prompt_dict,
                "prompt_values": [self.prompt_value],
                "json": True,
            }
        )
        llm_output = llm.run()

        return {
            **llm_output.get("extracted_responses")[0],
            "request_tokens": llm_output.get("request_tokens")[0],
            "response_tokens": llm_output.get("response_tokens")[0],
        }
```

In summary, these files work together to define a robust step in a larger workflow for interacting with LLMs, particularly focusing on prompt simplification and API integration.