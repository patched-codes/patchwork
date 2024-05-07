import json
import os
import tempfile
from pathlib import Path

from patchwork.steps import ScanDepscan


def test_run():
    inputs = {}
    # String content to be written to the package.lock file
    package_lock_content = """{
    "name": "example-javascript",
    "version": "0.0.1",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
          "name": "example-javascript",
          "version": "0.0.1",
          "dependencies": {
            "jquery": "3.0.0-alpha1"
          }
        },
        "node_modules/jquery": {
          "version": "3.0.0-alpha1",
          "resolved": "https://registry.npmjs.org/jquery/-/jquery-3.0.0-alpha1.tgz",
          "integrity": "sha512-agCHkB3RtPYzPifHRYPuxAoWFX+t09VtJKAzPOjUvts/qq5P/1SULEbdoY8hFUSS3eTY/03CMlSfaRAip0T36A=="
        }
    }
}"""

    # Create a temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        package_lock_path = Path(temp_dir) / "package-lock.json"
        with open(package_lock_path, "w") as f:
            f.write(package_lock_content)

        # Change cwd to the temporary directory
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)

            # Instantiate and run the ScanDepscan step
            result = ScanDepscan(inputs).run()

            # Verify the result
            sbom_vdr_file_path = result.get("sbom_vdr_file_path")
            assert sbom_vdr_file_path is not None

            # Check if the file exists and is a valid JSON
            assert os.path.exists(sbom_vdr_file_path)

            with open(sbom_vdr_file_path, "r") as f:
                json.load(f)  # This will raise an exception if the file is not a valid JSON

        finally:
            # Reset cwd
            os.chdir(original_cwd)
