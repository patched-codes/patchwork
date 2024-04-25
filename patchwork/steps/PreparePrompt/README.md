# PreparePrompt Class Documentation

## Overview

The `PreparePrompt` class extends the 'Step' class. It is designed to prepare prompt instructions by allowing the user to input specific keys and generating the corresponding prompt instructions.

This class requires specific keys to be provided on initialisation, and the `run` method later returns a dictionary with the path to the generated prompt file.

### Initialize method (`__init__`)

The `(self, inputs: dict)` method initializes the `PreparePrompt` class and takes a `dict` object as an input parameter. This dictionary should contain specific keys (as listed in the `required_keys` variable), specifically "prompt_template_file" and "prompt_id".

These keys carry out the following tasks:

- `prompt_template_file`: Path to the file containing the prompt template. This file should be a JSON file that follows a certain predefined structure to work with this class.
- `prompt_id`: This utilizes a specific template from the `prompt_template_file`.
- `prompt_value_file` (optional): If present, the method will load prompt values from this file instead of directly from the inputs.
- `prompt_values` (optional): If present, these prompt values will be used directly.

If the `prompt_value_file` or `prompt_values` are not provided, an error will be raised. If the JSON files for the templates or values fail to load, an error will also be raised.

### Run method

The `run` method of this class does not take any inputs. It iterates over the prompt values and each part of the prompt template, substitute placeholders in the template using the corresponding value, and consolidates all parts. This process is repeated for all prompt values, and the result is a list of prompts.

The resulting prompts are then saved to a temporary `.json` file, and the path to this file is returned in a dictionary with the key "prompt_file".

## Inputs

For initialization of class, the following keys are expected in the input dictionary:

- `prompt_template_file`: A string representing the file path of the prompt template. This is a required key.
- `prompt_id`: A string representing the ID of the prompt in the file. This is a required key.
- `prompt_value_file`: A string representing the file path of the prompt values file. Either this key or `prompt_values` is required.
- `prompt_values`: A dictionary of prompt values. Either this key or `prompt_value_file` is required.

## Outputs

The `run` method provides an output which is a dictionary with the following key:

- `prompt_file`: A string representing the path to the temporary json file storing the formatted prompts.