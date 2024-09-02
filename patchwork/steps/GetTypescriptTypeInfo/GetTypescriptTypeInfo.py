import os
import subprocess
from pathlib import Path

from patchwork.step import Step
from patchwork.steps.GetTypescriptTypeInfo.typed import GetTypescriptTypeInfoInputs, GetTypescriptTypeInfoOutputs


_DEFAULT_TS_FILE = Path(__file__).parent / "get_type_info.ts"


class GetTypescriptTypeInfo(Step, input_class=GetTypescriptTypeInfoInputs, output_class=GetTypescriptTypeInfoOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        required_keys = {"file_path", "variable_name"}
        if not all(key in inputs.keys() for key in required_keys):
            raise ValueError(f'Missing required data: "{required_keys}"')

        self.inputs = inputs

    def run(self) -> dict:
        file_path = self.inputs["file_path"]
        variable_name = self.inputs["variable_name"]

        cwd = Path.cwd()

        full_file_path = os.path.join(cwd, file_path)

        # Get the directory of the current script
        # current_dir = cwd

        # Construct the path to get_type_info.ts
        # get_type_info_path = os.path.join(current_dir, "get_type_info.ts")

        # Run the subprocess call
        subprocess.run(["tsx", _DEFAULT_TS_FILE, full_file_path, variable_name], check=True, cwd=cwd)

        # Read the output file
        output_path = os.path.join(cwd, "temp_output_declaration.txt")
        with open(output_path, "r") as f:
            type_info = f.read()

        # Clean up the temporary file
        os.remove(output_path)

        return {"type_information": type_info}
