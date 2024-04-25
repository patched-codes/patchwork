# CallOpenAI Class

This Python module contains a class `CallOpenAI` that is intended to make calls to the OpenAI API and get the response. It is designed to be used in the process of running machine learning models with OpenAI.

## Initialization method (__init__)

The initialization method `__init__()` is used to initialize the class with required arguments.

### Inputs

It takes a dictionary as an input. `inputs` dictionary should include the following keys:

- `"openai_api_key"`: The OpenAI API key. If not provided, it will try to fetch it from the environment variable `OPENAI_API_KEY`.
- `"prompt_file"`: The path to the JSON file that contains the prompts to be sent to OpenAI.
- `"model"`: The OpenAI model to be used.
- `"allow_truncated"`: A Boolean flag that, if set as `True`, will allow processing of truncated responses. By default, it is set to `False`.
- Keys starting with `"model_"`: These are arguments that will be passed to the OpenAI model.
- Keys starting with `"client_"`: These are arguments that will be passed to the OpenAI client.

### Errors

During initialization, it checks if all required keys are present in the dictionary. If not, it will raise a ValueError. If the `"prompt_file"` does not point to a file or the file is not in proper JSON format, it will raise ValueError.

## Run method

The `run()` method is used to send prompts to the OpenAI API and receive responses from it.

### Outputs

It returns a dictionary with the following keys:

- `"new_code"`: The path to a temporary JSON file which contains the responses received from the OpenAI API.
- `"openai_responses"`: A list containing the responses from OpenAI.