from __future__ import annotations

import re
import string
from pathlib import Path

import requests
from packageurl import PackageURL

from patchwork.common.utils.utils import defered_temp_file
from patchwork.logger import logger
from patchwork.step import Step

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


def generate_version_combinations(vuln_version, fixed_version):
    """
    Generate a list of tuples with different combinations of vulnerability and fixed versions,
    allowing for different prefixes like '', 'v', and 'rel/'.

    Args:
    - vuln_version (str): The vulnerable version in SemVer format.
    - fixed_version (str): The fixed version in SemVer format.

    Returns:
    - List[Tuple[str, str]]: A list of tuples representing different combinations of the input versions with various prefixes.
    """
    prefixes = ["", "v", "rel/"]
    combinations = set()

    # Function to transform pre-release versions to extended patch versions
    def convert_pre_release_to_patch(version):
        parts = version.split("-")
        if len(parts) > 1 and parts[1].startswith("pre."):
            pre_release_part = parts[1].split(".")[1]  # Assumes a single numeric identifier for simplification
            new_version = f"{parts[0]}.{pre_release_part}"
            return new_version
        return version

    # Generate combinations for given prefixes, including applying prefixes only to one version
    vuln_version_extended = convert_pre_release_to_patch(vuln_version)
    fixed_version_extended = convert_pre_release_to_patch(fixed_version)

    for vuln_prefix in prefixes:
        for fixed_prefix in prefixes:
            prefixed_vuln = f"{vuln_prefix}{vuln_version}" if vuln_prefix else vuln_version
            prefixed_fixed = f"{fixed_prefix}{fixed_version}" if fixed_prefix else fixed_version
            combinations.add((prefixed_vuln, prefixed_fixed))

            if vuln_version_extended != vuln_version or fixed_version_extended != fixed_version:
                prefixed_vuln_extended = (
                    f"{vuln_prefix}{vuln_version_extended}" if vuln_prefix else vuln_version_extended
                )
                prefixed_fixed_extended = (
                    f"{fixed_prefix}{fixed_version_extended}" if fixed_prefix else fixed_version_extended
                )
                combinations.add((prefixed_vuln_extended, prefixed_fixed_extended))

    return list(combinations)


def is_text_line(line):
    """Heuristic to determine if a line likely represents text."""
    printable = set(string.printable)
    return all(c in printable or c in "\n\r\t" for c in line)


def should_process_file(file_path, language_exts):
    """Determine if the file path matches the criteria for processing."""
    excluded_dirs = ["test", "tests", "example", "examples", "build", "builds"]
    # Check if any excluded directory is part of the file path
    return not any(
        f"/{dir}/" in file_path or file_path.startswith(f"{dir}/") or file_path.endswith(f"/{dir}")
        for dir in excluded_dirs
    ) and any(file_path.endswith(ext) for ext in language_exts)


def process_diff(diff_content, language_exts):
    """
    Process and filter a diff file's content.

    :param diff_content: The content of the diff file as a string.
    :param language_exts: A list of file extensions relevant to the programming language.
    :return: The processed diff content.
    """
    lines = diff_content.split("\n")
    processed_lines = []
    process_lines = False

    for line in lines:
        if line.startswith("diff --git"):
            # Example line: "diff --git a/src/main.py b/src/main.py"
            parts = line.split()
            if len(parts) > 2:
                file_path = parts[2][2:]  # Extract the file path from the diff header, removing the "a/" prefix
                process_lines = should_process_file(file_path, language_exts)
        if process_lines and is_text_line(line):
            processed_lines.append(line)

    return "\n".join(processed_lines)


def extract_diff_sections(diff_lines):
    """
    Extracts sections from a diff provided as a list of lines.

    Parameters:
    - diff_lines (list of str): The diff lines.

    Returns:
    - list of list of str: A list where each element is a section from the diff,
      with each section being a list of lines.
    """
    sections = []
    current_section = []

    for line in diff_lines:
        # Check if the line starts a new section
        if line.startswith("diff --git"):
            # If we already have a current section, save it before starting a new one
            if current_section:
                sections.append("\n".join(current_section))
                current_section = []
        # Add the line to the current section
        current_section.append(line)

    # Don't forget to add the last section if it exists
    if current_section:
        sections.append("\n".join(current_section))

    return sections


def get_diff_sections(diff_file_path: str | Path, language: str) -> list[str]:
    with open(diff_file_path, "r") as file:
        diff_content = file.read()

    diff_content = process_diff(diff_content, language_exts=_LANG_EXTENSIONS_.get(language))
    diff_sections = extract_diff_sections(diff_content.splitlines())
    return diff_sections


class ExtractDiff(Step):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        required_keys = {"update_info", "libraries_api_key", "github_api_key"}

        if not all(key in inputs.keys() for key in required_keys):
            raise ValueError(f'Missing required data: "{required_keys}"')

        self.libraries_api_key = inputs["libraries_api_key"]
        self.libraries_base_url = "https://libraries.io/api/"

        self.github_token = inputs["github_api_key"]
        self.update_info = inputs["update_info"]

        self.inputs = inputs

    def run(self) -> dict:
        regex = r"https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)"
        base_url = "https://api.github.com/repos/"
        update_info = self.update_info

        purl = PackageURL.from_string(update_info["purl"]).to_dict()
        platform_type = purl["type"]
        namespace = purl["namespace"]
        name = purl["name"]
        if namespace is not None:
            name = namespace + ":" + name
        vuln_version = update_info["vuln_version"]
        fixed_version = update_info["fixed_version"]
        info = requests.get(self.libraries_base_url + platform_type + "/" + name + "?api_key=" + self.libraries_api_key)
        if info.status_code != 200:
            logger.info(f"Unable to get repo url for library {name}")
            return {}

        repo_url = info.json()["repository_url"]
        try:
            match = re.match(regex, repo_url)
            repo = match.group("repo")
            owner = match.group("owner")
        except:
            logger.info(f"Unable to get extract repo and owner for repository_url: {repo_url}")
            return {}

        headers = {"Accept": "application/vnd.github.diff", "Authorization": f"Bearer {self.github_token}"}
        compare_url = base_url + owner + "/" + repo + "/compare/"

        temp_file_path = None

        for vuln_version, fixed_version in generate_version_combinations(vuln_version, fixed_version):
            diff_file = requests.get(compare_url + vuln_version + "..." + fixed_version, headers=headers)

            if diff_file.text.startswith("diff"):
                with defered_temp_file("w") as fp:
                    fp.write(diff_file.text)
                    temp_file_path = Path(fp.name)

        if temp_file_path is None:
            logger.info(
                f"Unable to generate diff for the repo {compare_url} between versions {vuln_version} and {fixed_version}"
            )
            return {}

        diff_sections = get_diff_sections(temp_file_path, _PURL_TO_LANGUAGE_.get(platform_type))
        extracted_data = []

        for diff_section in diff_sections:
            extracted_data.append({"diffSection": diff_section})

        return dict(prompt_values=extracted_data, library_name=name, platform_type=platform_type)
