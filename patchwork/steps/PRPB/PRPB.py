from patchwork.common.utils.utils import exclude_none_dict
from patchwork.step import Step
from patchwork.steps import PR
from patchwork.steps.PR.typed import PRInputs
from patchwork.steps.PRPB.typed import PRPBInputs, PRPBOutputs


class PRPB(Step, input_class=PRPBInputs, output_class=PRPBOutputs):

    def __init__(self, inputs):
        super().__init__(inputs)
        key_map = dict(path=inputs['path_key'])
        if inputs.get('title_key') is not None:
            key_map['commit_message'] = inputs['comment_title_key']
        if inputs.get('message_key') is not None:
            key_map['patch_message'] = inputs['comment_message_key']

        self.modified_files = []
        for modified_file in inputs.get('modified_files', []):
            converted_modified_file = {
                key: modified_file.get(mapped_key) for key, mapped_key in key_map.items()
            }
            self.modified_files.append(converted_modified_file)
        self.inputs = inputs

    def run(self):
        pr = PR({**self.inputs, 'modified_code_files': self.modified_files})
        pr_outputs = pr.run()

        return pr_outputs
