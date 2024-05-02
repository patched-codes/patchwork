import copy
import json
from pathlib import Path

import yaml

from patchwork.step import Step
from patchwork.steps import (
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

        number = 0
        modified_files = []

        if self.inputs.get("prompt_value_file") is not None:
            with open(self.inputs["prompt_value_file"], "r") as fp:
                vulns = json.load(fp)
                if len(vulns) > 0:
                    number = number + len(vulns[0]["Updates"])

        for i in range(self.n):
            if self.analyze_impact:
                analyze_inputs = copy.deepcopy(self.inputs)
                update_info_list = []

                if analyze_inputs.get("prompt_value_file") is not None:
                    with open(analyze_inputs["prompt_value_file"], "r") as fp:
                        vulns = json.load(fp)
                        if len(vulns) > 0:
                            update_info_list = vulns[0]["Updates"]

                for update_info in update_info_list:
                    analyze_inputs["update_info"] = update_info
                    outputs = ExtractDiff(analyze_inputs).run()
                    if len(outputs) == 0:
                        continue
                    analyze_inputs.update(outputs)
                    analyze_inputs["prompt_id"] = "getimpact"
                    analyze_inputs["response_partitions"] = {"impacted_methods": ["A. Impacted methods:", ""]}
                    outputs = PreparePrompt(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    outputs = CallLLM(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    outputs = ExtractModelResponse(analyze_inputs).run()
                    analyze_inputs.update(outputs)

                    # Do analysis on potential dependency upgrades and migrate the code as needed.
                    outputs = AnalyzeImpact(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    analyze_inputs["prompt_id"] = "migratecode"
                    analyze_inputs["response_partitions"] = {"patch": []}
                    outputs = PreparePrompt(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    outputs = CallLLM(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    outputs = ExtractModelResponse(analyze_inputs).run()
                    analyze_inputs.update(outputs)
                    outputs = ModifyCode(analyze_inputs).run()
                    modified_files = modified_files + outputs["modified_code_files"]

            self.inputs["prompt_id"] = "depupgrade"
            self.inputs["response_partitions"] = {"patch": []}
            outputs = PreparePrompt(self.inputs).run()
            self.inputs.update(outputs)
            outputs = CallLLM(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ExtractModelResponse(self.inputs).run()
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
            if self.inputs.get("prompt_value_file") is not None:
                with open(self.inputs["prompt_value_file"], "r") as fp:
                    vulns = json.load(fp)
                    if len(vulns) < 1:
                        break
                    number = number + len(vulns[0]["Updates"])

        self.inputs["pr_header"] = f"This pull request from patchwork fixes {number} vulnerabilities."
        outputs = CommitChanges(self.inputs).run()
        self.inputs.update(outputs)
        outputs = PreparePR(self.inputs).run()
        self.inputs.update(outputs)
        outputs = CreatePR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
