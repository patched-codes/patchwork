import os
from pathlib import Path

from patchwork.logger import logger
from patchwork.step import Step, StepStatus

_PURL_TO_LANGUAGE_ = {
    "pypi": "python",
    "npm": "javascript",
    "maven": "java",
    "golang": "go",
    "gem": "ruby",
}

_LANG_EXTENSIONS_ = {
    "python": [".py"],
    "java": [".java"],
    "javascript": [".js", "jsx", ".ts", ".tsx"],
    "go": [".go"],
    "ruby": [".rb"],
}


def find_dependency_usage(directory, dependency, language, methods):
    """
    Searches for the usage of a specific dependency in all relevant files within the given directory,
    according to the specified programming language, and identifies if any of the specified methods are called
    in those files.

    Parameters:
    - directory (str): The root directory of the project.
    - dependency (str): The name of the dependency to search for.
    - language (str): The programming language (e.g., 'python', 'java', 'javascript', 'typescript', 'go').
    - methods (list of str): A list of method names to search for in the usage context of the specified dependency.

    Returns:
    - A dictionary mapping file paths to lists of method names from the specified list that are called in the file.
    """
    dependency_usage = {}
    import_patterns = {
        "python": [f"import {dependency}", f"from {dependency} import"],
        "java": [f"import {dependency}."],
        "javascript": [f'import .* from "{dependency}"', f'require("{dependency}")'],
        "go": [f'import "{dependency}"', f"import {dependency} "],
    }

    # Define the file extensions and import patterns to look for based on the selected language
    file_extensions = _LANG_EXTENSIONS_.get(language, [])
    patterns = import_patterns.get(language, [])

    for root, dirs, files in os.walk(directory, topdown=True):
        # Skip directories starting with '.'
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                # Check for import usage
                import_usage_found = any(any(pattern in line for pattern in patterns) for line in lines)

                # If dependency is used, check for method calls
                if import_usage_found:
                    called_methods = set()
                    for line in lines:
                        for method in methods:
                            if f"{method}(" in line:
                                called_methods.add(method)
                    if called_methods:
                        dependency_usage[file_path] = list(called_methods)

    return dependency_usage


class AnalyzeImpact(Step):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        required_keys = {"extracted_responses", "library_name", "platform_type"}
        if not all(key in inputs.keys() for key in required_keys):
            raise ValueError(f'Missing required data: "{required_keys}"')

        self.inputs = inputs

    def run(self) -> dict:
        extracted_responses = self.inputs["extracted_responses"]
        if len(extracted_responses) == 0:
            self.set_status(StepStatus.SKIPPED, "No extracted responses found")
            return dict(files_to_patch=[])

        name = self.inputs["library_name"]
        platform_type = self.inputs["platform_type"]

        library_impacted_methods = {}
        for extracted_response in extracted_responses:
            response_text = extracted_response.get("impacted_methods")
            if response_text is None:
                continue

            count = 1

            search_text_format = "{count}. "
            search_text = search_text_format.format(count=count)
            start_idx = response_text.find(search_text)
            while start_idx != -1:
                end_idx = response_text.find(search_text_format.format(count=count + 1))
                if end_idx == -1:
                    end_idx = len(response_text)
                method_info = response_text[start_idx + len(search_text) : end_idx].strip()
                method_name, _, impact = method_info.partition(":\n")
                library_impacted_methods[method_name.strip()] = impact.strip()

                count += 1
                start_idx = response_text.find(search_text_format.format(count=count))

        impacted_files = find_dependency_usage(
            Path.cwd(), name, _PURL_TO_LANGUAGE_.get(platform_type), library_impacted_methods.keys()
        )
        if len(extracted_responses) != 0:
            logger.info(f"Impacted methods used from {name} library are : {impacted_files}")
        extracted_data = []

        for impacted_file in impacted_files:
            # Attempt to read the impacted_file's content
            try:
                with open(impacted_file, "r") as file:
                    file_content = file.read()
            except FileNotFoundError:
                logger.info(f"File not found in the current working directory: {impacted_file}")
                continue

            lines = file_content.splitlines(keepends=True)

            method_infos = []
            for method in impacted_files[impacted_file]:
                method_infos.append(f"Method name: {method} Change summary: {library_impacted_methods[method]}")

            data = dict(
                startLine=0,
                endLine=len(lines),
                uri=impacted_file,
                previousCode=file_content,
                methodInfoList="\n".join(method_infos),
            )
            extracted_data.append(data)

        return dict(files_to_patch=extracted_data)
