# Documentation for SimplifiedLLMOncePB Module

This documentation provides a detailed overview of the files and code involved in the `SimplifiedLLMOncePB` module. This module is used for configuring and running a simplified large language model (LLM) with specific input requirements and token-based authentication.

## Table of Contents
- [patchwork/steps/SimplifiedLLMOncePB/typed.py](#patchworkstepsSimplifiedLLMOncePBtypedpy)
- [patchwork/steps/SimplifiedLLMOncePB/__init__.py](#patchworkstepsSimplifiedLLMOncePB__init__py)
- [patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py](#patchworkstepsSimplifiedLLMOncePBSimplifiedLLMOncePBpy)

## patchwork/steps/SimplifiedLLMOncePB/typed.py

### Overview
Defines the input data structure for the `SimplifiedLLMOncePB` class, using typed dictionaries to enforce schema requirements.

### Inputs
- **`json_schema`**: Dictionary specifying the JSON schema for the expected response. Annotated with `StepTypeConfig(is_config=True)`.
- **`user_prompt`**: String containing the user's prompt. Annotated with `StepTypeConfig(is_config=True)`.
- **`prompt_value`**: Dictionary with values to be used within the prompt.
- **`system_prompt`** *(Optional)*: String containing the system's prompt. Annotated with `StepTypeConfig(is_config=True)`.
- **`model`** *(Optional)*: String specifying the model to be used. Annotated with `StepTypeConfig(is_config=True)`.
- **API Keys** *(Optional)*: Strings for different API keys (`openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`), each annotated with `StepTypeConfig(is_config=True)` and `or_op` to provide flexible authentication options.

### Usage
This file is mainly used to define the input types required by the `SimplifiedLLMOncePB` step. 

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

## patchwork/steps/SimplifiedLLMOncePB/__init__.py

### Overview
This is an empty initializer file for the `SimplifiedLLMOncePB` module.

### Purpose
Ensures that `SimplifiedLLMOncePB` can be treated as a package.

### Code
```python

```

---

## patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

### Overview
Implements the `SimplifiedLLMOncePB` class, a step for running an LLM with a single prompt and handling the JSON schema for responses.

### Inputs
- **`inputs`**: A dictionary containing all required and optional inputs defined in `SimplifiedLLMOncePBInputs`.

### Outputs
- **Response Dictionary**: A dictionary containing the LLM response, including the extracted responses and token counts.

### Methods
- **`__init__(self, inputs)`**: Initializes the object with the given inputs.
- **`__json_schema_as_suffix(self, prompt: str)`**: Formats the prompt to include the JSON schema.
- **`run(self)`**: Executes the LLM call and returns a dictionary with the response and token usage.

### Usage
1. Instantiate the `SimplifiedLLMOncePB` class with the required inputs.
2. Call the `run` method to execute the LLM and retrieve the response.

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

---

Feel free to reach out if you have any questions or need further assistance!