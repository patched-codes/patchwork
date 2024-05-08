from collections import defaultdict
from textwrap import indent

from patchwork.logger import logger
from patchwork.step import Step


class PreparePR(Step):
    required_keys = {"modified_code_files"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        if len(inputs["modified_code_files"]) < 1:
            logger.warning("No modified files to prepare a PR for.")
        self.modified_code_files = inputs["modified_code_files"]

        self.header = f"This pull request from patched fixes {len(self.modified_code_files)} issues."
        if "pr_header" in inputs.keys():
            self.header = inputs["pr_header"]

    def run(self) -> dict:
        modified_code_files_grouped_by_path = defaultdict(list)
        for modified_code_file in self.modified_code_files:
            modified_code_files_grouped_by_path[modified_code_file["path"]].append(modified_code_file)

        file_comment_parts = []
        for path, items in modified_code_files_grouped_by_path.items():
            path_placeholder = "{{" + path + "}}"
            file_part = f"File changed: [{path}]({path_placeholder})"

            chunk_comment_parts = []
            for item in items:
                start_line = item.get("start_line")
                end_line = item.get("end_line")
                title = item.get("commit_message", "")
                patch_msg = item.get("patch_message", "")
                if title == "" and patch_msg == "":
                    continue

                placeholder_inner_text = path
                if start_line is not None and end_line is not None:
                    placeholder_inner_text = f"{path}:{start_line+1}:{end_line}"
                chunk_link = "{{" + placeholder_inner_text + "}}"

                if title != "" and patch_msg == "":
                    expandable = f"\n  [{title.strip()}]({chunk_link})"
                elif title == "" and patch_msg != "":
                    expandable = (
                        f"<details>"
                        f"<summary>({placeholder_inner_text})[{chunk_link}]</summary>"
                        f"{indent(patch_msg.strip(), '  ')}"
                        f"</details>"
                    )
                else:
                    # when both title and patch_msg are present
                    expandable = (
                        f"<details>"
                        f"<summary>[{title.strip()}]({chunk_link})</summary>"
                        f"{indent(patch_msg.strip(), '  ')}"
                        f"</details>"
                    )
                chunk_comment_parts.append(expandable)

            msg = f"""\
<div markdown="1">

* {file_part}{''.join(chunk_comment_parts)}

</div>"""
            file_comment_parts.append(msg)

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(
            pr_body="\n\n".join([self.header, "------", *file_comment_parts]),
        )
