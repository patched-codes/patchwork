from pathlib import Path

import yaml
import json
import tempfile

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
    CreatePR,
)

_DEFAULT_INPUT_FILE = Path(__file__).parent / "defaults.yml"
_DEFAULT_PROMPT_JSON = Path(__file__).parent / "prompt.json"

class ResolveIssue(Step):
    def __init__(self, inputs: dict):
        final_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())
                    
        if final_inputs is None:
            final_inputs = {}
        final_inputs.update(inputs)
            
        if "prompt_template_file" not in final_inputs.keys():
            final_inputs["prompt_template_file"] = _DEFAULT_PROMPT_JSON
        
        final_inputs["pr_title"] = f"PatchWork {self.__class__.__name__}"
        final_inputs["branch_prefix"] = f"{self.__class__.__name__.lower()}-"
        
        self.fix_issue = bool(final_inputs.get("fix_issue", False))
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
        
        if self.fix_issue:
            extracted_code_contexts = []
            # Call LLM to make necessary updates to files to resolve the issue
            for result in self.inputs["embedding_results"]:
                with open(result["path"], "r") as file:
                    file_content = file.read()
                lines = file_content.splitlines(keepends=True)
                extracted_code_contexts.append(
                    {
                        "uri": result["path"],
                        "startLine": 0,
                        "endLine": len(lines),
                        "affectedCode": file_content,
                        "messageText": "\n".join(self.inputs["texts"]),
                    })
            
            self.inputs["prompt_values"] = extracted_code_contexts
            
            # Save extracted data to JSON
            output_file = Path(tempfile.mktemp(".json"))
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(extracted_code_contexts, f, indent=2)
                
            self.inputs["code_file"] = output_file
            self.inputs["prompt_id"] = "resolve_issue"
            self.inputs["response_partitions"] = {"patch": []}
            outputs = PreparePrompt(self.inputs).run()
            self.inputs.update(outputs)
            outputs = CallOpenAI(self.inputs).run()
            self.inputs.update(outputs)
            outputs = ExtractModelResponse(self.inputs).run()
            self.inputs.update(outputs)

            # Modify code files with the suggested changes
            outputs = ModifyCode(self.inputs).run()
            self.inputs.update(outputs)

            # Commit changes and create PR
            outputs = CommitChanges(self.inputs).run()
            self.inputs.update(outputs)
            outputs = CreatePR(self.inputs).run()
            self.inputs.update(outputs)

        return self.inputs
