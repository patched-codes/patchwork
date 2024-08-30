# Documentation for SimplifiedLLMOncePB Step

## Overview

The `SimplifiedLLMOncePB` module is designed to interact with a language model (LLM) by sending prompts and receiving structured JSON responses. This module is part of the `patchwork` framework and leverages several configurations for accepting various API keys. The primary objective of the module is to streamline the process of interacting with LLMs using specified prompts and receiving responses formatted according to a predefined JSON schema.

## Files

### `typed.py`

#### Inputs

- **`json_schema`**: Defines the output format for the model. (`Dict[str, Any]`)
- **`user_prompt`**: The primary user prompt to be sent to the model. (`str`)
- **`prompt_value`**: Additional values to be included in the prompt. (`Dict[str, Any]`)
- **`system_prompt` (optional)**: An optional system-level prompt for additional context. (`str`)
- **`model`**: Specifies the model to be used. (`str`)
- **`openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`**: API keys for different platforms, one of which must be provided.

#### Exports (Output)

This file mainly defines the input structure for the `SimplifiedLLMOncePB` step but does not generate output by itself.

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
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["openai_api_key", "google_api_key", "anthropic_api_key"], msg=f"""Model API key not found. Please login at: "{TOKEN_URL}" Please go to the Integration's tab and generate an API key. Please copy the access token that is generated, and add `--patched_api_key=<token>` to the command line. If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.""")]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])]
```

### `__init__.py`

Empty file, often used to mark a directory as a Python package.

```python

```

### `SimplifiedLLMOncePB.py`

#### Inputs

- Accepts an instance of `SimplifiedLLMOncePBInputs`.

#### Outputs

- Returns a dictionary containing:
  - **Extracted responses** formatted according to the provided `json_schema`.
  - **Request tokens** from the LLM API.
  - **Response tokens** from the LLM API.

#### Usage

1. Instantiate `SimplifiedLLMOncePB` with the required inputs.
2. Call the `run` method to get a structured JSON response from the LLM.

#### Code

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
        return f"""{prompt}\nRespond only with the following json format, do not include any additional information:\n{json.dumps(self.json_schema)}"""

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

## Conclusion

The `SimplifiedLLMOncePB` module provides a structured way to interact with language models, ensuring the outputs conform to a specific JSON schema. The module is configurable with various API keys and supports both user and system prompts. This makes it a versatile tool for developers working with LLMs in a variety of contexts.