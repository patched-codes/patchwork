from __future__ import annotations

from patchwork.step import Step
from patchwork.steps import ModifyCode
from patchwork.steps.ModifyCodePB.typed import ModifyCodePBInputs, ModifyCodePBOutputs


class ModifyCodePB(Step, input_class=ModifyCodePBInputs, output_class=ModifyCodePBOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        self.files_with_patch = inputs["files_with_patch"]

    def run(self) -> dict:
        modify_code = ModifyCode(
            {
                "files_to_patch": [
                    dict(
                        uri=self.files_with_patch.get("file_path"),
                        startLine=self.files_with_patch.get("start_line"),
                        endLine=self.files_with_patch.get("end_line"),
                    )
                ],
                "extracted_responses": [
                    dict(
                        patch=self.files_with_patch.get("patch"),
                    )
                ],
            }
        )
        modified_code_files = modify_code.run()
        return dict(**modified_code_files[0])
