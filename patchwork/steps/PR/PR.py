from patchwork.common.utils.utils import exclude_none_dict
from patchwork.step import Step
from patchwork.steps.CommitChanges.CommitChanges import CommitChanges
from patchwork.steps.CreatePR.CreatePR import CreatePR
from patchwork.steps.PR.typed import PRInputs, PROutputs
from patchwork.steps.PreparePR.PreparePR import PreparePR


class PR(Step, input_class=PRInputs, output_class=PROutputs):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.inputs = inputs
        self.__handle_modified_code_files()

    def __handle_modified_code_files(self):
        if self.inputs.get("modified_code_files") is not None:
            return

        self.inputs["modified_code_files"] = []

        input_modified_files = self.inputs.get("modified_files")
        if input_modified_files is None or len(input_modified_files) < 1:
            return

        key_map = dict()
        key_map["path"] = self.inputs.get("path_key", "path")
        if self.inputs.get("comment_title_key") is not None:
            key_map["commit_message"] = self.inputs["comment_title_key"]
        if self.inputs.get("comment_message_key") is not None:
            key_map["patch_message"] = self.inputs["comment_message_key"]

        modified_files = []
        if isinstance(input_modified_files, list):
            for modified_file in input_modified_files:
                converted_modified_file = {key: modified_file.get(mapped_key) for key, mapped_key in key_map.items()}
                if converted_modified_file.get("path") is None:
                    continue
                modified_files.append(converted_modified_file)
        elif isinstance(input_modified_files, dict):
            converted_modified_file = {key: input_modified_files.get(mapped_key) for key, mapped_key in key_map.items()}
            modified_files.append(converted_modified_file)
        elif isinstance(input_modified_files, str):
            converted_modified_file = {"path": input_modified_files}
            modified_files.append(converted_modified_file)

        self.inputs["modified_code_files"] = modified_files

    def run(self):
        commit_changes = CommitChanges(self.inputs)
        commit_changes_output = commit_changes.run()
        self.set_status(commit_changes.status, commit_changes.status_message)

        prepare_pr = PreparePR(self.inputs)
        prepare_pr_output = prepare_pr.run()
        self.set_status(prepare_pr.status, prepare_pr.status_message)

        create_pr = CreatePR(
            dict(
                base_branch=commit_changes_output.get("base_branch"),
                target_branch=commit_changes_output.get("target_branch"),
                pr_body=prepare_pr_output.get("pr_body"),
                **self.inputs,
            )
        )
        create_pr_outputs = create_pr.run()
        self.set_status(create_pr.status, create_pr.status_message)

        return exclude_none_dict(
            dict(
                base_branch=commit_changes_output.get("base_branch"),
                target_branch=commit_changes_output.get("target_branch"),
                pr_url=create_pr_outputs.get("pr_url"),
                pr_number=create_pr_outputs.get("pr_number"),
                pr_title=prepare_pr_output.get("pr_title"),
                pr_body=prepare_pr_output.get("pr_body"),
            )
        )
