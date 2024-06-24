This documentation provides details about a codebase related to extracting code contexts from SARIF files. It includes Python modules related to context strategies for different languages and the main extraction logic in `ExtractCode.py`.

## Inputs
- The main input is a SARIF file path.
- Other optional inputs include `context_size` and `vulnerability_limit`.

## Outputs
The code extracts relevant code contexts from the SARIF file based on specified criteria and saves the extracted data into a JSON file. The outputs include the following:
- `prompt_value_file`: Path to the JSON file.
- `code_file`: Path to the JSON file.
- `extracted_code_contexts`: List containing extracted code contexts with context start and end lines, URI, and message text.