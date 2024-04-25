# Code Documentation: ExtractCode Class

This documentation focuses on the `ExtractCode` class in the `ExtractCode.py` script, highlighting the `__init__` and `run` methods.

## Overview

The script parses Secure Software Assurance Embedded Results Aggregation Framework (SARIF) data and extracts code segments that are indicated to contain vulnerabilities. The results of the process are then saved as a JSON file. The context from which the affected code segment is extracted can be controlled by specifying the token count and severity level of the vulnerabilities to consider.

## Input

The `__init__` method requires a dictionary `inputs` with the key `"sarif_file_path"`. An additional three optional keys can be included in the `inputs` dictionary:

- `"context_size"`: Specifies the token count of the context to extract around the affected code. Default is 1000.
- `"vulnerability_limit"`: Limits the number of vulnerabilities extracted from the SARIF data. Default is 10.
- `"severity"`: The minimum severity level of vulnerabilities to consider. Default is "UNKNOWN".

## Output

The `run` method returns a dictionary with the following keys:

- `"code_file"`: A Path object pointing to the output JSON file.
- `"prompt_values"`: A list of extracted vulnerability data, with each list item being a dictionary containing the information about one vulnerability.

Each item in `"prompt_values"` is structured as follows:

- `"uri"`: The relative path of the file containing the vulnerability, relative to the base (root project) path.
- `"startLine"`: The starting line number of the context from the source code file.
- `"endLine"`: The ending line number of the context from the source code file.
- `"affectedCode"`: The extracted segment of source code containing the vulnerability.
- `"messageText"`: The message associated with the vulnerability. 

Note that all indices are 0-based and inclusive. If no context is found for a particular vulnerability, the item is not included in `"prompt_values"`.