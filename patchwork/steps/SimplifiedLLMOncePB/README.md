# Documentation for `patchwork/steps/SimplifiedLLMOncePB`

## Overview
The `SimplifiedLLMOncePB` module is designed to provide an abstraction for calling a Language Learning Model (LLM) service with simplified configurations. The module comprises three primary files:

- `typed.py`: Defines the input schema using TypedDict and annotations.
- `SimplifiedLLMOncePB.py`: Implements the main functionality of the `SimplifiedLLMOncePB` class, which inherits from the `Step` class.
- `__init__.py`: An empty file to mark the directory as a Python package.

## Files

### 1. patchwork/steps/SimplifiedLLMOncePB/typed.py

#### Description
Defines the schema for inputs required to initialize and run the `SimplifiedLLMOncePB` step. This schema makes use of `TypedDict` for typed dictionaries and `Annotated` for additional metadata annotations.

#### Inputs
- **json_schema**: A dictionary representing the JSON schema for the inputs. This is configurable.
- **user_prompt**: A string containing the user's prompt. This is configurable.
- **prompt_value**: A dictionary containing prompt values.
- **system_prompt** (optional): A string containing system-level prompts. This is configurable.
- **model**: A string representing the model's identifier. This is configurable.
- **openai_api_key**: An optional API key for OpenAI. Interchangeable with other API keys.
- **anthropic_api_key**: An optional API key for Anthropic. Interchangeable with other API keys.
- **patched_api_key**: A general-purpose API key configurable through multiple providers.
- **google_api_key**: An optional API key for Google. Interchangeable with other API keys.

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
    openai_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "anthropic_api_key"])]
    anthropic_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "google_api_key", "openai_api_key"])]
    patched_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["openai_api_key", "google_api_key", "anthropic_api_key"], msg=f"""...""")]
    google_api_key: Annotated[str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])]
```

### 2. patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py

#### Description
Implements the main functionality of the `SimplifiedLLMOncePB` step. The class handles the preparation of prompts and the invocation of the language model.

#### Inputs
The input parameters for this class are defined in `SimplifiedLLMOncePBInputs` from `typed.py`. Upon initialization, it assigns values for user prompts, system prompts (if any), prompt values, and JSON schema to corresponding attributes.

#### Outputs
The `run` method returns a dictionary that includes:
- **Extracted Responses**: The JSON data extracted from LLM responses.
- **Request Tokens**: The number of tokens in the request.
- **Response Tokens**: The number of tokens in the response.

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
            prompt_dict = dict(prompt_system=self.system, prompt_user=self.user)
        else:
            prompt_dict = dict(prompt_user=self.user)

        llm = SimplifiedLLM({**self.inputs, **prompt_dict, "prompt_values": [self.prompt_value], "json": True, "json_example": self.json_example})
        llm_output = llm.run()

        return {
            **llm_output.get("extracted_responses")[0],
            "request_tokens": llm_output.get("request_tokens")[0],
            "response_tokens": llm_output.get("response_tokens")[0],
        }
```

### 3. patchwork/steps/SimplifiedLLMOncePB/__init__.py

#### Description
An empty file that marks the directory as a Python package. This allows importing of modules from this directory.

#### Code
```python

```

## Summary
The `SimplifiedLLMOncePB` module offers a streamlined approach for integrating LLM services by simplifying the input requirements and facilitating easy use of multiple API keys. By defining a clear schema and implementing core functionality in separate files, the module allows for comprehensive and flexible utilization of text-based AI models.