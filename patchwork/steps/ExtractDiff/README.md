# ExtractDiff Class Documentation

This documentation covers the `ExtractDiff` class which is used for comparison of semantic versions (vulnerable vs fixed) of a software package, where the vulnerable version has a security vulnerability and the fixed version repairs it. A diff is created for these two versions, which is processed and converted into sections. This information is then stored as JSON.

## Class Initialization (init method)

### Input

- `inputs` dictionary that includes:
    - `'github_api_key'`: API key required for GitHub connectivity.
    - `'libraries_api_key'`: API key required for libraries.io connectivity.
    - `'update_info'`: Dictionary containing information about the update, including the purl (Package URL), and the vulnerable and fixed versions of the package.

## Method: run
The run function is responsible for executing the essential functionality of this class i.e., extracting, processing, and storing the diffs.

### Output

- Returns a `dictionary` with the following keys:
    - `'prompt_value_file'`: Path to the output file containing the extracted data, in JSON format.
    - `'library_name'`: Name of the library for which diff was extracted.
    - `'platform_type'`: The type of platform of the package for which the update information is provided. This is determined by the purl in `update_info`.

Note: If the function fails at any point (unable to get repo URL, unable to extract repo and owner, or unable to generate the diff), it will return an empty dictionary `{}`.