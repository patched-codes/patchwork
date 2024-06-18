import atexit
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from patchwork.common.utils.dependency import import_with_dependency_group
from patchwork.logger import logger
from patchwork.step import Step


def is_cdxgen_installed():
    """Check if cdxgen is installed."""
    try:
        # Attempt to run cdxgen --version to check if it's installed
        subprocess.run(["cdxgen", "--version"], capture_output=True, check=True)
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
        subprocess.run(["npm", "install", "-g", "@cyclonedx/cdxgen"], check=True)
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
        logger.info(f"Run started {self.__class__.__name__}")
        import_with_dependency_group("depscan")
        install_cdxgen()

        self.language = inputs.get("language", None)

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
        temp_file_path = Path(tempfile.mkdtemp())
        atexit.register(shutil.rmtree, temp_file_path, ignore_errors=True, onerror=None)

        cmd = [
            "depscan",
            "--reports-dir",
            str(temp_file_path),
        ]

        if self.language is not None:
            cmd.append("-t")
            cmd.append(self.language)
            sbom_vdr_file_name = "sbom-" + self.language
        else:
            sbom_vdr_file_name = "sbom-universal"

        p = subprocess.run(cmd, capture_output=True, text=True)

        sbom_vdr_file_path = temp_file_path / f"{sbom_vdr_file_name}.vdr.json"
        try:
            with open(sbom_vdr_file_path, "r") as f:
                sbom_values = json.load(f)
        except json.JSONDecodeError as e:
            logger.debug(e)
            raise ValueError(f"Error reading SBOM VDR file from Depscan")
        except FileNotFoundError as e:
            logger.debug(e)
            raise ValueError(f"SBOM VDR file not found from Depscan")

        logger.info(f"Run completed {self.__class__.__name__}")
        return {"sbom_vdr_values": sbom_values}
