import json
import os
import subprocess
import tempfile
from pathlib import Path

from semver.version import Version

from patchwork.common.utils.dependency import import_with_dependency_group
from patchwork.logger import logger
from patchwork.step import Step

__target_cdxgen_version = "10.7.1"


def is_cdxgen_installed():
    """Check if cdxgen is installed."""
    try:
        # Attempt to run cdxgen --version to check if it's installed
        p = subprocess.run(["cdxgen", "--version"], capture_output=True, check=True)
        logger.debug(f"cdxgen version: {p.stdout}")
        cdxgen_version = Version.parse(p.stdout.strip())
        if cdxgen_version.compare(__target_cdxgen_version) > 0:
            logger.debug(
                f"cdxgen version {cdxgen_version} is installed, but version {__target_cdxgen_version} is required."
            )
            raise ValueError(
                f"cdxgen version {cdxgen_version} is installed, but version {__target_cdxgen_version} is required."
            )

        return True
    except subprocess.CalledProcessError as e:
        err = e
    except FileNotFoundError as e:
        err = e
    # If the command fails, cdxgen is not installed
    logger.info(f"cdxgen is not installed: {err}")
    return False


def install_cdxgen():
    """Install cdxgen using npm if it's not already installed."""
    if not is_cdxgen_installed():
        logger.info(f"Installing now...")
        # Install cdxgen globally using npm
        subprocess.run(["npm", "install", "-g", f"@cyclonedx/cdxgen@{__target_cdxgen_version}"], check=True)
        logger.info(f"cdxgen installed successfully.")
    else:
        logger.debug(f"cdxgen is already installed.")


class ScanDepscan(Step):
    def __init__(self, inputs: dict):
        """
        Initializes an instance of the class.

        This method logs the start of the run, including the name of the class being instantiated.
        It then checks if 'cdxgen' is installed on the system. If 'cdxgen' is not installed, it attempts to install it.

        Parameters:
        - inputs (dict): A dictionary of inputs required for initializing the class. The structure and content
                        of this dictionary will depend on the specific requirements of the class.

        Side Effects:
        - Logs the start of the run to the application's logger, indicating which class is being instantiated.
        - Checks for the presence of the 'cdxgen' command-line tool. If 'cdxgen' is not found, it installs 'cdxgen'
        globally using npm. This might require internet access and appropriate permissions to install global npm packages.

        Note:
        - This method assumes that npm (Node Package Manager) is installed and accessible in the system's PATH.
        - Depending on system configuration, administrative privileges may be required to install global npm packages.
        """
        super().__init__(inputs)
        import_with_dependency_group("depscan")
        install_cdxgen()

        self.language = inputs.get("language", None)
        self.license = inputs.get("license", None)

    def run(self) -> dict:
        """
        Executes the 'depscan' command-line tool, generating an SBOM (Software Bill of Materials) report.

        This method performs the following operations:
        - Generates a unique, temporary file path and constructs a directory path from it. This directory is intended
        to store the 'depscan' reports but note that the directory is not created automatically by this method.
        - Runs the 'depscan' tool with the specified reports directory. The 'depscan' command is expected to generate
        an SBOM report in the 'sbom-universal.vdr.json' file within the specified directory.
        - Logs the completion of the run, including the name of the class that executed the method.

        Returns:
        - A dictionary containing the path to the generated SBOM report file. The key for this path is 'sbom_vdr_file_path'.

        Side Effects:
        - A 'depscan' command is executed, which may modify files in the specified directory and generate network traffic
        if 'depscan' queries external sources for vulnerability data.
        - Logs the start and completion of the operation to the application's logger.

        Note:
        - This method assumes that 'depscan' is installed and accessible in the system's PATH.
        - The generated temporary directory path is based on a temporary file path and is manipulated to be a directory path;
        however, the directory itself is not automatically created by this method.
        - The caller is responsible for ensuring that the 'depscan' tool can run successfully and that the specified
        temporary directory exists and is writable.
        """
        # Generate a unique temporary file path
        with tempfile.TemporaryDirectory() as temp_file_path:
            cmd = [
                "depscan",
                "--debug",
                "--reports-dir",
                temp_file_path,
            ]

            if self.language is not None:
                cmd.extend(["-t", self.language])
                sbom_vdr_file_name = "sbom-" + self.language
            else:
                sbom_vdr_file_name = "sbom-universal"

            env = os.environ.copy()
            if self.license is not None:
                env["FETCH_LICENSE"] = "true"

            try:
                p = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd(), env=env)
            except subprocess.CalledProcessError as e:
                logger.debug("Command execution failed.")
                logger.debug("stdout:\n" + e.stdout)
                logger.debug("stderr:\n" + e.stderr)
                raise RuntimeError("Subprocess command execution failed") from e
            except Exception as e:
                logger.debug("Unexpected error during command execution")
                logger.debug(e)
                raise RuntimeError("Unexpected error during Subprocess execution") from e

            sbom_vdr_file_path = Path(temp_file_path) / f"{sbom_vdr_file_name}.vdr.json"
            try:
                with open(sbom_vdr_file_path, "r") as f:
                    sbom_values = json.load(f)
            except json.JSONDecodeError as e:
                logger.debug(e)
                raise ValueError(f"Error reading SBOM VDR file from Depscan")
            except FileNotFoundError as e:
                logger.debug("stdout:\n" + p.stdout)
                logger.debug("stderr:\n" + p.stderr)
                logger.debug(e)
                raise ValueError(f"SBOM VDR file not found from Depscan")

        return {"sbom_vdr_values": sbom_values}
