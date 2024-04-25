# CallCode2Prompt Class

This document describes the CallCode2Prompt class contained within the CallCode2Prompt.py file. This class is designed to invoke the "code2prompt" tool on a specified directory, extract data relating to a generated prompt, and return this data presented in a specific format.

## __init__ method

The `__init__` method is used to initialize an instance of the CallCode2Prompt class. 

### Input
- `inputs`: A dictionary that should contain the following key:
  - `folder_path`: The path to the directory where the code to convert into a prompt is located.
- Optional keys in `inputs` include:
  - `filter`: A filter to apply to the code conversion process, if applicable.
  - `suppress_comments`: A boolean value that dictates whether comments should be suppressed during the code conversion process. Default is False.

The `__init__` method will raise a ValueError if the `folder_path` key is not found in the `inputs` dictionary. 

## run method

The `run` method calls the "code2prompt" process on the folder path specified in the `inputs` when initializing the CallCode2Prompt instance. It organizes the results and returns them in a specific format.

### Output
The run method returns a dictionary containing two keys:
- `prompt_value_file`: Points to a temporary JSON file that contains the full extracted data from the code conversion process.
- `code_file`: Points to the same temporary JSON file as `prompt_value_file`.

The dictionary, and consequently the JSON file, contains various keys about the generated prompt:
- `fullContent`: The entire content of the extracted prompt in markdown.
- `uri`: The path to the README.md file in which the prompt is stored.
- `startLine`: The starting line number of the prompt content in the README file, usually 0.
- `endLine`: The last line number of the prompt in the README file, equals to the total number of lines.