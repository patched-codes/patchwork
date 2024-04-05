## Code Documentation

### Inputs
- This code defines a class `PreparePrompt` that is inherited from a `Step` class.
- The class takes a dictionary `inputs` as a parameter in its constructor, expecting keys `prompt_template_file`, `prompt_id`, `prompt_value_file`, and `prompt_values`.
- The `inputs` dictionary should contain the required keys specified in the `required_keys` set.

### Outputs
- The `run` method of the `PreparePrompt` class generates prompt data based on template files and values provided in `inputs`.
- It processes the template file to create prompt data with values substituted from the given value files or values directly provided.
- The generated prompt data is then saved into a JSON file, and its path is returned as an output in a dictionary format.

### Usage
- This code is likely to be used to generate prompt data based on a template and specific values.
- One would need to create an instance of the `PreparePrompt` class, passing the required inputs like `prompt_template_file`, `prompt_id`, `prompt_value_file`, and `prompt_values`.
- The `run` method can be called to process the inputs and generate the prompt file.
- The output dictionary containing the path to the generated prompt file can be used for further processing or logging.