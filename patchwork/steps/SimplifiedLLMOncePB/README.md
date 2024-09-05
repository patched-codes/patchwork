# Documentation: SimplifiedLLMOncePB Module

## Overview

This module provides functionality for interacting with a Simplified Large Language Model (LLM) in a streamlined manner. It contains the class definitions and typing required to set up and execute a single LLM query with various input options and configurations.

## Files

### 1. `patchwork/steps/SimplifiedLLMOncePB/typed.py`

#### Description

This file defines the input types and configurations required by the `SimplifiedLLMOncePB` class. It uses Python's typing extensions to annotate the expected data types.

#### Inputs

- **json_schema**: A dictionary defining the JSON schema, required.
- **user_prompt**: A string that contains the user's input prompt, required.
- **prompt_value**: A dictionary containing values to be used within the prompt, required.
- **system_prompt**: An optional string for additional system-level prompt context.
- **model**: A string defining the model to be used, optional.
- **openai_api_key**: An OpenAI API key, optional.
- **anthropic_api_key**: An Anthropic API key, optional.
- **patched_api_key**: A custom patched API key, optional, with specific instructions provided.
- **google_api_key**: A Google API key, optional.

#### Code
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

### 2. `patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py`

#### Description

This file contains the class definition for `SimplifiedLLMOncePB`, which sets up the required inputs and runs the LLM query by delegating to the `SimplifiedLLM` class.

#### Inputs

The class expects an instance of `SimplifiedLLMOncePBInputs` with fields as described above.

#### Outputs

- **extracted_responses**: The first extracted response from the LLM.
- **request_tokens**: Tokens used in the request.
- **response_tokens**: Tokens received in the response.

#### Code

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

### 3. `patchwork/steps/SimplifiedLLMOncePB/__init__.py`

#### Description

An empty initialization file to denote this directory as a Python package.

#### Code
```python

```

## Usage

This module is designed to be used within a larger framework that involves calling LLMs with specific configurations. The `SimplifiedLLMOncePB` class can be instantiated with appropriate inputs and then executed to get simplified and structured responses from the LLM.

```python
from patchwork.steps.SimplifiedLLMOncePB.SimplifiedLLMOncePB import SimplifiedLLMOncePB
from patchwork.steps.SimplifiedLLMOncePB.typed import SimplifiedLLMOncePBInputs

inputs = SimplifiedLLMOncePBInputs(
    user_prompt="What is the weather like today?",
    prompt_value={},
    json_schema={}
    # Other optional configurations
)

simplified_llm_once_pb = SimplifiedLLMOncePB(inputs)
response = simplified_llm_once_pb.run()

print(response)
```

This code sets up the required inputs, instantiates the class, and executes the LLM query, thereby returning the expected outputs.