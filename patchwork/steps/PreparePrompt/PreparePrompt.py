from __future__ import annotations

import json
import random
import string
from pathlib import Path

import chevron
from chevron import render

from patchwork.common.constants import PROMPT_TEMPLATE_FILE_KEY
from patchwork.logger import logger
from patchwork.step import Step, StepStatus

chevron.render.__globals__["_html_escape"] = lambda string: string


def _find_by_prompt_template_file(prompt_template_file: str | None, prompt_id: str | None) -> list[dict] | None:
    if prompt_template_file is None or prompt_id is None:
        return None

    prompt_template_file = Path(prompt_template_file)
    if not prompt_template_file.is_file():
        logger.warning(f"PromptTemplateFile[{prompt_template_file}] does not exist")
        return None

    try:
        with open(prompt_template_file, "r") as fp:
            prompt_templates = json.load(fp)
    except json.JSONDecodeError as e:
        logger.warning(f"Invalid Json at PromptTemplateFile[{prompt_template_file}]")
        return None

    prompt_templates = next((prompt for prompt in prompt_templates if prompt.get("id") == prompt_id), None)
    if prompt_templates is None:
        logger.warning(f"Unable to find PromptId[{prompt_id}] in PromptTemplateFile[{prompt_template_file}]")

    prompt_template = prompt_templates.get("prompts")
    if prompt_template is None:
        logger.warning(
            f"No key `prompts` found for PromptId[{prompt_id}] in PromptTemplateFile[{prompt_template_file}]"
        )

    return prompt_template


class PreparePrompt(Step):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        self.prompt_template = _find_by_prompt_template_file(
            inputs.get(PROMPT_TEMPLATE_FILE_KEY), inputs.get("prompt_id")
        )
        if self.prompt_template is None:
            self.prompt_template = inputs.get("prompt_template")
        if self.prompt_template is None:
            raise ValueError(
                f'Missing required data: "{PROMPT_TEMPLATE_FILE_KEY}" with "prompt_id" or "prompt_template"'
            )

        prompt_value_file = inputs.get("prompt_value_file")
        prompt_values = inputs.get("prompt_values")
        if prompt_value_file is None and prompt_values is None:
            raise ValueError('Missing required data: "prompt_value_file" or "prompt_values"')
        if prompt_values is None and not Path(prompt_value_file).is_file():
            raise ValueError(f"Prompt Value File {prompt_value_file} does not exist")

        if prompt_values is None:
            try:
                with open(Path(prompt_value_file), "r") as fp:
                    prompt_values = json.load(fp)
            except json.JSONDecodeError as e:
                raise ValueError(f'Invalid Json Prompt Value file "{prompt_value_file}": {e}')

        self.prompt_values = prompt_values

    def run(self) -> dict:
        if len(self.prompt_values) == 0:
            self.set_status(StepStatus.SKIPPED, "No prompt values provided")
            return dict(prompts=[])

        prompts = []
        for prompt_value in self.prompt_values:
            dict_value = prompt_value
            if not isinstance(dict_value, dict):
                dict_value = prompt_value.__dict__

            prompt = []
            for prompt_part in self.prompt_template:
                prompt_instance = {}
                for key, value in prompt_part.items():
                    new_value = render(
                        template=value,
                        data=dict_value,
                        partials_path=None,
                        partials_ext="".join(random.choices(string.ascii_uppercase + string.digits, k=32)),
                        partials_dict=dict(),
                    )
                    prompt_instance[key] = new_value
                prompt.append(prompt_instance)
            prompts.append(prompt)

        return dict(prompts=prompts)
