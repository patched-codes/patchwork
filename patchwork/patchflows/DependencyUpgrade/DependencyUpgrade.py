import copy
from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.step import Step
from patchwork.steps import (
    LLM,
    PR,
    AnalyzeImpact,
    CallLLM,
    CommitChanges,
    CreatePR,
    ExtractDiff,
    ExtractModelResponse,
    ExtractPackageManagerFile,
    ModifyCode,
    PreparePR,
    PreparePrompt,
    ScanDepscan,
)

_DEFAULT_PROMPT_JSON = Path(__file__).parent / "dependency_upgrade_prompt.json"
_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


class DependencyUpgrade(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            AnalyzeImpact,
            CallLLM,
            CommitChanges,
            CreatePR,
            ExtractDiff,
            ExtractModelResponse,
            ExtractPackageManagerFile,
            ModifyCode,
            PreparePR,
            PreparePrompt,
            ScanDepscan,
        )

        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        if "branch_prefix" not in final_inputs.keys():
            final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        if "prompt_template_file" not in final_inputs.keys():
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"

        self.n = int(final_inputs.get("n", 1))
        self.analyze_impact = bool(final_inputs.get("analyze_impact", False))
        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = ScanDepscan(self.inputs).run()
        self.inputs.update(outputs)
        outputs = ExtractPackageManagerFile(self.inputs).run()
        self.inputs.update(outputs)
        self.inputs["prompt_values"] = self.inputs.get("files_to_patch", [])

        number = 0
        modified_files = []

        if self.inputs.get("prompt_values") is not None:
            vulns = self.inputs.get("prompt_values")[0]
            number = number + len(vulns["Updates"])

        for i in range(self.n):
            if self.analyze_impact:
                analyze_inputs = copy.deepcopy(self.inputs)
                update_info_list = []

                if analyze_inputs.get("prompt_values") is not None:
                    vulns = analyze_inputs.get("prompt_values")[0]
                    update_info_list = vulns["Updates"]

                for update_info in update_info_list:
                    analyze_inputs["update_info"] = update_info
                    outputs = ExtractDiff(analyze_inputs).run()
                    if len(outputs) == 0:
                        continue
                    analyze_inputs.update(outputs)
                    analyze_inputs["prompt_id"] = "getimpact"
                    analyze_inputs["response_partitions"] = {"impacted_methods": ["A. Impacted methods:", ""]}
                    outputs = LLM(analyze_inputs).run()
                    analyze_inputs.update(outputs)

                    # Do analysis on potential dependency upgrades and migrate the code as needed.
                    outputs = AnalyzeImpact(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    analyze_inputs["prompt_id"] = "migratecode"
                    analyze_inputs["response_partitions"] = {"patch": []}
                    analyze_inputs["prompt_values"] = outputs["files_to_patch"]
                    outputs = LLM(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    outputs = ModifyCode(analyze_inputs).run()
                    modified_files = modified_files + outputs["modified_code_files"]

            self.inputs["prompt_id"] = "depupgrade"
            outputs = LLM(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ModifyCode(self.inputs).run()
            self.inputs.update(outputs)
            self.inputs["modified_code_files"] = self.inputs["modified_code_files"] + modified_files

            if i == self.n - 1:
                break

            # validation
            outputs = ScanDepscan(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ExtractPackageManagerFile(self.inputs).run()
            self.inputs.update(outputs)
            if self.inputs.get("prompt_values") is not None:
                vulns = self.inputs.get("prompt_values")[0]
                if len(vulns) < 1:
                    break
                number = number + len(vulns["Updates"])

        self.inputs["pr_header"] = f"This pull request from patchwork fixes {number} vulnerabilities."
        outputs = PR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
