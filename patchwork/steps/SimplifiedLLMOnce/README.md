## `patchwork/steps/SimplifiedLLMOnce/typed.py`

### Inputs
- Defines types for required inputs for a step called SimplifiedLLMOnce.
- Includes input types related to prompting users, model selection, API keys, and response partitions.

### Outputs
- Defines output types related to prompting, the response from an API call, and extracted responses.

## `patchwork/steps/SimplifiedLLMOnce/SimplifiedLLMOnce.py`

### Code
- Imports necessary modules for a step called SimplifiedLLMOnce.
- Defines a class SimplifiedLLMOnce inheriting from Step.
- Initializes the step with required inputs, checking for missing data.
- Executes the step's functionality by preparing prompts, making an API call, and extracting responses.
- Returns processed data after excluding any None values.