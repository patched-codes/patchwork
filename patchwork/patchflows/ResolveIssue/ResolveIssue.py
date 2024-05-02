import yaml
import json
from pathlib import Path
from patchwork.step import Step
from patchwork.steps import (
    CreateIssueComment, 
    GenerateCodeRepositoryEmbeddings, 
    QueryEmbeddings, 
    ReadIssues, 
    PreparePrompt, 
    CallOpenAI, 
    ExtractModelResponse, 
    ModifyCode, 
    CommitChanges, 
    CreatePR
)

_DEFAULT_INPUT_FILE = Path(__file__).parent / ".." / "config" / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / ".." / "config" / "prompt.json"

def load_default_config(file: Path):
    if file.is_file():
        with open(file, 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    return {}

def load_default_prompt(file: Path):
    if file.is_file():
        with open(file, 'r') as f:
            return json.load(f)
    return {}

class ResolveIssue(Step):
    def __init__(self, inputs: dict):
        final_inputs = {**load_default_config(_DEFAULT_INPUT_FILE), **inputs}
        final_inputs["prompt_values"] = load_default_prompt(_DEFAULT_PROMPT_JSON)
        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"

        self.inputs = final_inputs

    def run(self) -> dict:
        outputs = GenerateCodeRepositoryEmbeddings(self.inputs).run()
        self.inputs.update(outputs)

        outputs = ReadIssues(self.inputs).run()
        self.inputs.update(outputs)

        self.inputs["texts"] = self.inputs["issue_text"]

        outputs = QueryEmbeddings(self.inputs).run()
        self.inputs.update(outputs)

        issue_list_text = "* " + "\n* ".join([result["path"] for result in self.inputs["embedding_results"]])
        self.inputs[
            "issue_text"
        ] = f"""\
The following files in the repository may be relevant to the issue:

------

{issue_list_text}
"""

        outputs = CreateIssueComment(self.inputs).run()
        self.inputs.update(outputs)

        outputs = PreparePrompt(self.inputs).run()
        self.inputs.update(outputs)

        outputs = CallOpenAI(self.inputs).run()
        self.inputs.update(outputs)

        outputs = ExtractModelResponse(self.inputs).run()
        self.inputs.update(outputs)

        outputs = ModifyCode(self.inputs).run()
        self.inputs.update(outputs)

        outputs = CommitChanges(self.inputs).run()
        self.inputs.update(outputs)

        outputs = CreatePR(self.inputs).run()
        self.inputs.update(outputs)

        return self.inputs
