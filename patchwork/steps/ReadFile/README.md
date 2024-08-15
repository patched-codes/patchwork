## Inputs
- typed.py defines two TypedDict classes: ReadFileInputs with a `file_path` attribute of type str and ReadFileOutputs with a `file_content` attribute of type str.
- ReadFile.py implements the ReadFile class inherited from Step. It takes ReadFileInputs as inputs in the constructor.
- The class ensures that all required keys are present in the inputs and raises a ValueError if any are missing.
- It reads a file based on the provided `file_path` input using `open_with_chardet` and returns the file content in a dictionary with the key `file_content`.

## Outputs
- The code provides the structure and functionality for reading a file based on the path provided in the inputs and returning the content of the file.