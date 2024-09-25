# SimplifiedLLMOncePB Documentation

## Overview
The `SimplifiedLLMOncePB` module encapsulates functionality to run a simplified large language model (LLM) in a specific configuration. This module is designed to manage user prompts, system prompts, and API keys needed to interact with various LLM services. 

This documentation covers the three main files in the module:
- `typed.py`: Defines the input types and configurations.
- `__init__.py`: Initializes the module.
- `SimplifiedLLMOncePB.py`: Implements the core functionality to interact with the LLM.

## Files

### 1. `typed.py`

#### Description
This file defines the input types and types required by the `SimplifiedLLMOncePB` step using Python's `TypedDict` and `Annotated` for enhanced type safety and validation.

#### Inputs
- `json_schema` (Dict[str, Any]): The schema defining the structure of the JSON payload.
- `user_prompt` (str): The user's input prompt.
- `prompt_value` (Dict[str, Any]): The values to be substituted in the prompt.
- Optional keys:
  - `system_prompt` (str): The system defined prompt.
  - `model` (str): The identifier for the LLM model.
  - API keys (`openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key`): Various possible API keys required for different models or integrations.

#### Example Code
```python
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
            msg="""Model API key not found. Please login at: "{TOKEN_URL}"...""",
        ),
    ]
    google_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["patched_api_key", "openai_api_key", "anthropic_api_key"])
    ]
```

### 2. `__init__.py`

#### Description
An empty file used to mark the directory as a Python package.

#### Example Code
```python
```

### 3. `SimplifiedLLMOncePB.py`

#### Description
Implements the core functionality of the `SimplifiedLLMOncePB` step. This class prepares the prompts and inputs required to call the LLM and handle its output.

#### Inputs
- The inputs are defined as per the `SimplifiedLLMOncePBInputs` class in `typed.py`.

#### Outputs
- A dictionary containing the user's prompt results along with request and response tokens.

#### Example Code
```python
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
        self.set_status(llm.status, llm.status_message)

        return {
            **llm_output.get("extracted_responses")[0],
            "request_tokens": llm_output.get("request_tokens")[0],
            "response_tokens": llm_output.get("response_tokens")[0],
        }
```

## Usage

1. **Initialize inputs**: Define the necessary inputs like `user_prompt`, `system_prompt`, `model`, API keys, and others as per the `SimplifiedLLMOncePBInputs` class.
2. **Instantiate the `SimplifiedLLMOncePB` class**: Pass in the inputs during instantiation.
3. **Run the instance**: Call the `run()` method to execute the prompt against the LLM and retrieve the output.

This module is designed to be flexible with several possible API keys and model configurations, making it adaptable to various LLM providers.