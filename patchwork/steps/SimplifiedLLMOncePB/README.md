# patchwork/steps/SimplifiedLLMOncePB Documentation

## [patchwork/steps/SimplifiedLLMOncePB/typed.py](#patchworkstepsSimplifiedLLMOncePBtyped.py)

### Purpose
This file defines the input typing for the `SimplifiedLLMOncePB` step, using Python's `TypedDict` and other typing annotations. This standardizes the input format and provides configuration options for the various keys used in the step.

### Inputs
- `json_schema` (Dict[str, Any]): A JSON schema that defines the expected output structure.
- `user_prompt` (str): The main user prompt for the language model.
- `prompt_value` (Dict[str, Any]): Additional values to customize the prompt.
- `Optional[system_prompt]` (str): Optional system-level instructions for the prompt.
- API Keys:
  - `model` (str): The model to be used.
  - `openai_api_key`, `anthropic_api_key`, `patched_api_key`, `google_api_key` (str): API keys for different providers. Must provide at least one.

### Usage
This typing becomes essential when initializing and validating the `SimplifiedLLMOncePB` class's inputs, ensuring the inputs match the expected configuration schema.

### Code Example
```python
class SimplifiedLLMOncePBInputs(__SimplifiedLLMOncePBInputsRequired, total=False):
    # Definitions of required and optional inputs.
```

## [patchwork/steps/SimplifiedLLMOncePB/__init__.py](#patchworkstepsSimplifiedLLMOncePB__init__.py)

### Purpose
An empty `__init__.py` file that allows the `SimplifiedLLMOncePB` module to be recognized as a package.

### Usage
No specific usage or inputs. It is a standard file for making a directory a Python package.

### Code Example
```python
# No code
```

## [patchwork/steps/SimplifiedLLMOncePB/SimplifiedLLMOncePB.py](#patchworkstepsSimplifiedLLMOncePBSimplifiedLLMOncePB.py)

### Purpose
Implements the `SimplifiedLLMOncePB` class, which encapsulates functionality to communicate with a language model using the provided prompts and configurations. 

### Inputs
- Initialized with a dictionary complying with `SimplifiedLLMOncePBInputs`.

### Key Methods
- `__init__(self, inputs)`: Initializes the step with provided inputs.
- `__json_schema_as_suffix(self, prompt: str)`: Formats the prompt by appending the JSON schema.
- `run(self) -> dict`: Runs the language model (`SimplifiedLLM`) using the prepared prompts and returns the parsed response.

### Outputs
- A dictionary containing parsed responses from the language model, inclusive of request and response tokens.

### Usage
Used for calling a language model with specific prompt formatting and configurations. Typically serves as part of a pipeline to generate controlled outputs from an LLM.

### Code Example
```python
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

This file and functionality will be used by developers needing to integrate a step in their pipelines that calls an LLM with predefined and well-structured prompts, ensuring the output adheres to a specific JSON schema.