# BrowserUse Documentation

## Overview
The `BrowserUse` module provides functionality to automate browser interactions using an LLM-powered agent. This module enables tasks to be performed in a web browser environment, with the agent navigating websites, filling forms, clicking buttons, and extracting information as needed. The module supports multiple LLM providers and can generate visual recordings of the browser session for debugging purposes.

This documentation covers the three main files in the module:
- `typed.py`: Defines the input and output types.
- `__init__.py`: Initializes the module.
- `BrowserUse.py`: Implements the core functionality for browser automation.

## Files

### 1. `typed.py`

#### Description
This file defines the input and output types required by the `BrowserUse` step using Python's `TypedDict` and `Annotated` for enhanced type safety and validation.

#### Inputs
- `task` (str): The description of the task to be performed in the browser.
- `json_example_schema` (str): Optional schema for formatting the output as JSON.
- API keys (`openai_api_key`, `anthropic_api_key`, `google_api_key`): Various possible API keys required for different LLM providers.

#### Outputs
- `result` (str): The final result of the browser interaction.
- `request_tokens` (int): The number of tokens used in the request.
- `response_tokens` (int): The number of tokens used in the response.

#### Example Code
```python
class BrowserUseInputs(TypedDict, total=False):
    task: str
    json_example_schema: str
    openai_api_key: Annotated[
        str,
        StepTypeConfig(is_config=True, or_op=["google_api_key", "anthropic_api_key"]),
    ]
    anthropic_api_key: Annotated[
        str, StepTypeConfig(is_config=True, or_op=["google_api_key", "openai_api_key"])
    ]
    google_api_key: Annotated[
        str,
        StepTypeConfig(is_config=True, or_op=["openai_api_key", "anthropic_api_key"]),
    ]


class BrowserUseOutputs(TypedDict):
    result: str
    request_tokens: int
    response_tokens: int
```

### 2. `__init__.py`

#### Description
An empty file used to mark the directory as a Python package.

#### Example Code
```python
```

### 3. `BrowserUse.py`

#### Description
Implements the core functionality of the `BrowserUse` step. This class initializes a browser instance, sets up the LLM agent, and executes the specified task in the browser environment.

#### Inputs
- The inputs are defined as per the `BrowserUseInputs` class in `typed.py`.

#### Outputs
- A dictionary containing the browser interaction history and final result, optionally formatted as JSON according to the provided schema.

#### Example Code
```python
class BrowserUse(Step, input_class=BrowserUseInputs, output_class=BrowserUseOutputs):
    required_keys = {"task"}

    def __init__(self, inputs):
        super().__init__(inputs)

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.browser = Browser(config=config)
        if "google_api_key" in self.inputs:
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash", google_api_key=self.inputs["google_api_key"]
            )
        elif "openai_api_key" in self.inputs:
            self.llm = ChatOpenAI(model="gpt-4o", api_key=self.inputs["openai_api_key"])
        elif "anthropic_api_key" in self.inputs:
            self.llm = ChatAnthropic(
                model="claude-3-7-sonnet-latest",
                api_key=self.inputs["anthropic_api_key"],
            )

    def run(self) -> dict:
        agent = Agent(
            browser=self.browser,
            task=self.inputs["task"],
            llm=self.llm,
            generate_gif=f"agent_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.gif"
            if self.inputs["debug"]
            else False,
            validate_output=True,
        )

        loop = asyncio.new_event_loop()
        self.history = loop.run_until_complete(agent.run())

        if self.inputs["json_example_schema"]:
            return self.__format_history_as_json()

        return {"history": self.history, "result": self.history.final_result()}
```

## Usage

1. **Initialize inputs**: Define the necessary inputs including the `task` description and at least one API key for the LLM provider.

2. **Instantiate the `BrowserUse` class**: Pass in the inputs during instantiation.

3. **Run the instance**: Call the `run()` method to execute the browser automation task and retrieve the output.

### Example

```python
from patchwork.steps.BrowserUse import BrowserUse

# Define inputs
inputs = {
    "task": "Go to example.com and extract the main heading",
    "openai_api_key": "your-openai-api-key",
    "debug": True  # Enable GIF recording for debugging
}

# Create and run the BrowserUse step
browser_step = BrowserUse(inputs)
result = browser_step.run()

# Access the result
print(result["result"])
```

## Features

- **Multi-LLM Support**: Compatible with OpenAI, Anthropic, and Google Generative AI models.
- **Debug Mode**: Can generate GIF recordings of browser sessions for debugging purposes.
- **JSON Output**: Ability to format the output as JSON according to a provided schema.
- **Headless Operation**: Browser runs in headless mode by default for efficiency.

This module is designed to automate browser-based tasks using LLM agents, making it useful for web scraping, form filling, and other web automation scenarios.
