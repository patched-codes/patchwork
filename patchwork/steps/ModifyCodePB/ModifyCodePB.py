from __future__ import annotations

from patchwork.step import Step
from patchwork.steps import ModifyCode
from patchwork.steps.ModifyCodePB.typed import ModifyCodePBInputs, ModifyCodePBOutputs


class ModifyCodePB(Step, input_class=ModifyCodePBInputs, output_class=ModifyCodePBOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        self.file_path = inputs["file_path"]
        self.start_line = inputs["start_line"]
        self.end_line = inputs["end_line"]
        self.patch = inputs["patch"]

    def run(self) -> dict:
        modify_code = ModifyCode(
            {
                "files_to_patch": [
                    dict(
                        uri=self.file_path,
                        startLine=self.start_line,
                        endLine=self.end_line,
                    )
                ],
                "extracted_responses": [
                    dict(
                        patch=self.patch,
                    )
                ],
            }
        )
        modified_code_files = modify_code.run()
        return dict(**modified_code_files["modified_code_files"][0])
