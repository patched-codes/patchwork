import json
import os
import re
from collections import defaultdict
from pathlib import Path

import semver
from packageurl import PackageURL

from patchwork.logger import logger
from patchwork.step import Step

# Define a mapping from CVSS severity level strings to numbers
SEVERITY_LEVELS = {"none": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}


def to_semver(version_string):
    """
    Transform an input version string into a proper Semantic Versioning formatted string.

    Args:
    - version_string (str): A version string that may include 'RELEASE', or be in formats like '2.4' or '0.3m'.

    Returns:
    - str: A string formatted according to Semantic Versioning standards, with default patch version as 0
           and pre-release identifiers properly formatted.
    """
    # Extended regular expression to match various version parts: major, minor, optional patch, and optional pre-release/metadata
    pattern = r"^(\d+)\.(\d+)(?:\.(\d+))?([A-Za-z]*)(?:\.([A-Za-z0-9]+))?$"
    match = re.match(pattern, version_string)

    if not match:
        raise ValueError("Input string is not in a recognized version format")

    # Extract version components with possible default values
    major, minor, patch, prerelease_direct, prerelease = match.groups("0")

    # Combine direct pre-release (like 'm' in '0.3m') with any additional identifiers
    prerelease_combined = prerelease_direct or prerelease

    # Reformat if there's a pre-release or other identifiers
    if prerelease_combined:
        return f"{major}.{minor}.{patch}-pre.{prerelease_combined}"
    else:
        return f"{major}.{minor}.{patch}"


def find_package_manager_files(directory, purl):
    """
    Identifies all possible package manager files for a given PURL in the specified directory, without searching subdirectories.
    Adds support for Gradle.

    Parameters:
    - directory (str): The root directory of the project.
    - purl (str): The Package URL of the dependency.

    Returns:
    - A list of paths to package manager files relevant to the PURL's type, found in the specified directory.
    """
    purl = PackageURL.from_string(purl)
    package_type = purl.to_dict()["type"]
    package_manager_files = {
        "pypi": ["requirements.txt", "Pipfile", "pyproject.toml"],
        "maven": ["pom.xml", "build.gradle", "build.gradle.kts"],
        "npm": ["package.json", "yarn.lock"],
        "golang": ["go.mod", "go.sum"],
    }

    relevant_files = package_manager_files.get(package_type, [])
    found_files = []

    # Directly list files in the specified directory
    try:
        for file in os.listdir(directory):
            if file in relevant_files:
                found_files.append(os.path.join(directory, file))
    except FileNotFoundError:
        logger.info(f"The directory {directory} was not found.")

    return found_files


class ExtractPackageManagerFile(Step):
    required_keys = {}

    def __init__(self, inputs: dict):
        """
        Initializes an instance of the class, setting up necessary validations and preparations
        for data extraction based on the provided input parameters.

        This method performs the following actions:
        - Logs the initiation of a run with the class name.
        - Validates that the input dictionary contains all required keys. Specifically, it checks
        for the presence of 'sbom_vdr_file_path', which should point to the SBOM VDR file.
        - Validates that the provided SBOM VDR file path exists and is a file. If not, it raises an error.
        - Prepares the instance for data extraction by initializing `extracted_data` as an empty list.

        Parameters:
        - inputs (dict): A dictionary containing input parameters for the instance. This must include
                        'sbom_vdr_file_path' key with a valid file path as its value.

        Raises:
        - ValueError: If the input dictionary does not contain all required keys or if the provided
                    SBOM VDR file path does not exist or is not a file.

        After successful initialization, the instance is ready to perform data extraction operations
        with its `extracted_data` attribute prepared for storing the results.
        """
        super().__init__(inputs)
        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        # Validate and set the SBOM VDR file path
        sbom_vdr_file_path = inputs.get("sbom_vdr_file_path")
        if sbom_vdr_file_path is not None:
            sbom_vdr_file_path = Path(sbom_vdr_file_path)
            if not sbom_vdr_file_path.is_file():
                raise ValueError(f'SBOM VDR file path does not exist or is not a file: "{sbom_vdr_file_path}"')
            with open(sbom_vdr_file_path, "r") as file:
                self.sbom_vdr_values = json.load(file)
        elif "sbom_vdr_values" in inputs.keys():
            self.sbom_vdr_values = inputs["sbom_vdr_values"]
        else:
            raise ValueError('"sbom_vdr_file_path" or "sbom_vdr_values" not found in inputs')

        self.package_manager_file = inputs.get("package_manager_file", None)

        self.upgrade_threshold = inputs.get("upgrade_threshold", "major")

        self.severity_threshold_level = SEVERITY_LEVELS.get(inputs.get("severity", "none").lower())

        # Prepare for data extraction
        self.extracted_data = []

    def run(self) -> dict:
        """
        Processes the SBOM VDR data to extract information about components and vulnerabilities,
        maps PURLs to their source files, identifies affected and unaffected versions, and compiles
        this data into a structured format. Finally, it saves the extracted data to a temporary JSON file.

        The method performs several key operations:
        1. Loads the SBOM VDR data from the file specified by `self.sbom_vdr_file_path`.
        2. Iterates over each component to map PURLs to source file paths.
        3. Processes each vulnerability to identify affected and unaffected versions,
        associating them with the corresponding source files.
        4. Attempts to read the content of each source file, logging an error if a file is not found.
        5. Compiles the processed data into a list stored in `self.extracted_data`,
        which includes the content of package manager files and updates information.
        6. Saves the extracted data to a temporary JSON file, logging the completion of the operation.

        Returns:
            A dictionary containing paths to the generated prompt value and code files, which are the same in this context.
            The key 'prompt_value_file' refers to the path of the file containing the extracted data,
            and 'code_file' also points to this same file.

        Raises:
            FileNotFoundError: If any specified source file in the SBOM VDR data cannot be found.

        Note:
            This method assumes that the SBOM VDR file is correctly formatted and accessible. It also
            assumes that the source files referenced within the SBOM VDR data are accessible for reading.
            The method logs detailed information about its execution status, including any file access issues.
        """
        components = self.sbom_vdr_values.get("components", [])
        # Initialize a dictionary to hold the mapping of purls to SrcFiles
        purl_to_srcfile = {}

        # Iterate over each component in the components list from SBOM VDR data
        for component in components:
            purl = component.get("purl", "")
            if self.package_manager_file is not None:
                src_file = self.package_manager_file
            else:
                found_src_files = find_package_manager_files(Path.cwd(), purl)
                if len(found_src_files) > 1:
                    logger.info(
                        f"{len(found_src_files)} package manager files found in the current working directory for {purl}. Use the package_manager_file argument to specify the one to update."
                    )
                    continue
                elif len(found_src_files) == 0:
                    logger.info(
                        f"No package manager files found in the current working directory for {purl}. Use the package_manager_file argument to specify the file."
                    )
                    continue
                else:
                    src_file = found_src_files[0]

            # Add the mapping to the dictionary if both purl and src_file are found
            if purl and src_file:
                purl_to_srcfile[purl] = src_file

        # Initialize a dictionary to hold the final structure
        result = {}

        # Process each vulnerabiility in SBOM VDR data
        purl_list = []
        for vul in self.sbom_vdr_values.get("vulnerabilities", []):
            severity = ""
            for rating in vul.get("ratings", []):
                severity = rating.get("severity", "")

            if severity != "" and SEVERITY_LEVELS.get(severity.lower(), 9999) < self.severity_threshold_level:
                continue

            ref = ""
            fixed_version = None
            vuln_version = ""
            for affect in vul.get("affects", []):
                ref = affect.get("ref", "")
                src_file = purl_to_srcfile.get(ref, "")

                for version in affect.get("versions", []):
                    if version.get("status", "") == "affected":
                        vuln_version = version.get("version", "")
                    elif version.get("status", "") == "unaffected":
                        fixed_version = version.get("version", "")

            if fixed_version is None:
                continue

            try:
                fixed_semver = to_semver(fixed_version)
                vuln_semver = to_semver(vuln_version)
                fixed_semver = semver.Version.parse(fixed_semver)
                vuln_semver = semver.Version.parse(vuln_semver)
            except ValueError as e:
                logger.info(f"Error while parsing versions for library {ref}: {e}")
                continue

            if (
                (self.upgrade_threshold.lower() == "major")
                or (self.upgrade_threshold.lower() == "minor" and fixed_semver.major == vuln_semver.major)
                or (
                    self.upgrade_threshold.lower() == "patch"
                    and fixed_semver.major == vuln_semver.major
                    and fixed_semver.minor == vuln_semver.minor
                )
            ):
                # Prepare the update info
                update_info = {"purl": ref, "vuln_version": vuln_version, "fixed_version": fixed_version}

                # If this is the first entry for this src_file, initialize the structure
                if src_file not in result:
                    result[src_file] = defaultdict(list)
                if ref not in purl_list:
                    result[src_file]["Updates"].append(update_info)
                    purl_list.append(ref)

        for src_file, data in result.items():
            # Attempt to read the src_file's content
            try:
                with open(src_file, "r") as file:
                    file_content = file.read()
            except FileNotFoundError:
                logger.info(f"File not found in the current working directory: {src_file}")
                continue

            lines = file_content.splitlines(keepends=True)
            # Update the structure with the PackageManagerFile content
            update_msg = ""
            for update_info in data["Updates"]:
                update_msg = (
                    update_msg
                    + "Upgrade library "
                    + update_info["purl"]
                    + " from "
                    + update_info["vuln_version"]
                    + " to "
                    + update_info["fixed_version"]
                    + "\n"
                )

            data["PackageManagerFile"] = file_content
            data["UpdateMsg"] = update_msg
            data["uri"] = src_file
            data["startLine"] = 0
            data["endLine"] = len(lines)
            self.extracted_data.append(data)

        return dict(files_to_patch=self.extracted_data)
