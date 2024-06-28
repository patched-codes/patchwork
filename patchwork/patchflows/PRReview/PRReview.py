from pathlib import Path

import yaml

from patchwork.common.utils.progress_bar import PatchflowProgressBar
from patchwork.step import Step
from patchwork.steps import (
    LLM,
    CallLLM,
    CreatePRComment,
    ExtractModelResponse,
    PreparePR,
    PreparePrompt,
    ReadPRDiffs,
)

_DEFAULT_PROMPT_JSON = Path(__file__).parent / "pr_review_prompt.json"
_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"


_NONE = "none"
_SHORT = "short"
_LONG = "long"
_SUMMARY_LEVEL = {
    _NONE: 0,
    _SHORT: 1,
    _LONG: 2,
}


class PRReview(Step):
    def __init__(self, inputs: dict):
        PatchflowProgressBar(self).register_steps(
            CallLLM,
            CreatePRComment,
            ExtractModelResponse,
            PreparePR,
            PreparePrompt,
            ReadPRDiffs,
        )
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
        final_inputs.update(inputs)

        if "prompt_template_file" not in final_inputs.keys():
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON

        diff_summary = final_inputs.get("diff_summary", _LONG)
        if diff_summary.lower() not in _SUMMARY_LEVEL.keys():
            raise ValueError(f"Invalid diff_summary, accepted diff_summary values: {_SUMMARY_LEVEL.keys()}")
        self.verbosity = _SUMMARY_LEVEL[diff_summary.lower()]

        self.is_suggestion_required = bool(final_inputs.get("diff_suggestion"))

        self.inputs = final_inputs

    def run(self) -> dict:
        if self.verbosity == _SUMMARY_LEVEL[_NONE]:
            return dict()

        outputs = ReadPRDiffs(self.inputs).run()
        self.inputs.update(outputs)

        other_fields = ""
        if self.is_suggestion_required:
            other_fields = "B. Suggestion:\n<Improvement suggestion>"
        for prompt_values in self.inputs["prompt_values"]:
            prompt_values["other_fields"] = other_fields

        self.inputs["prompt_id"] = "diffreview"
        self.inputs["response_partitions"] = {
            "summary": ["A. Summary:", ""],
            "suggestion": ["B. Suggestion:", "A. Summary:"],
        }
        outputs = LLM(self.inputs).run()
        self.inputs.update(outputs)

        summaries = []
        for response, prompt_values in zip(self.inputs["extracted_responses"], self.inputs["prompt_values"]):
            summary = {}
            if "path" in prompt_values.keys():
                summary["path"] = prompt_values["path"]
            if "summary" in response.keys():
                summary["commit_message"] = response["summary"]
            if "suggestion" in response.keys():
                summary["patch_message"] = response["suggestion"]
            summaries.append(summary)

        header = ""
        if self.verbosity > _SUMMARY_LEVEL[_SHORT]:
            filtered_summaries = [summary["commit_message"] for summary in summaries]
            self.inputs["prompt_id"] = "diffreview_summary"
            self.inputs["prompt_values"] = [{"diffreviews": "\n".join(filtered_summaries)}]

            outputs = PreparePrompt(self.inputs).run()
            self.inputs.update(outputs)
            outputs = CallLLM(self.inputs).run()
            self.inputs.update(outputs)
            header = self.inputs["openai_responses"][0]

        self.inputs["pr_header"] = header
        self.inputs["modified_code_files"] = summaries
        outputs = PreparePR(self.inputs).run()
        self.inputs.update(outputs)

        self.inputs["pr_comments"] = [{"body": self.inputs["pr_body"]}]
        outputs = CreatePRComment(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
