## ExtractModelResponse.py

### Inputs:
- The code defines a class `ExtractModelResponse` that inherits from `Step`.
- The `__init__` method of the class takes a dictionary `inputs` as a parameter.
- The required data keys in the `inputs` dictionary are checked to raise a `ValueError` if any key is missing.
- The `openai_responses` key from the `inputs` dictionary is assigned to `self.openai_responses`.
- The `response_partitions` key from the `inputs` dictionary is assigned to `self.partitions`.
  
### Outputs:
- The `run` method is defined to extract responses based on specified partitions from the `openai_responses`.
- If no partitions are specified, a log is generated and an empty response dictionary is returned.
- For each `openai_response`, it partitions the response based on the specified partitions and stores the extracted response in the `outputs`.
- Finally, a dictionary containing the extracted responses is returned.

### Usage:
- The `ExtractModelResponse` class is intended to extract model responses based on specified partitions.
- Users can instantiate the class by passing the required inputs where `openai_responses` key is mandatory.
- After instantiation, the `run` method can be called to extract responses based on the specified partitions and get the extracted responses as output.