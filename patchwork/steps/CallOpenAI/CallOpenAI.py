import json
import os
import tempfile
from pathlib import Path
from pprint import pformat
from textwrap import indent

from openai import OpenAI

from patchwork.logger import logger
from patchwork.step import Step


class CallOpenAI(Step):
    required_keys = {"openai_api_key", "prompt_file"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        # Set 'openai_key' from inputs or environment if not already set
        inputs.setdefault("openai_api_key", os.environ.get("OPENAI_API_KEY"))

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.model = inputs["model"]
        self.model_args = {key[len("model_") :]: value for key, value in inputs.items() if key.startswith("model_")}
        self.client_args = {key[len("client_") :]: value for key, value in inputs.items() if key.startswith("client_")}

        self.openai_api_key = inputs["openai_api_key"]
        self.prompt_file = Path(inputs["prompt_file"])
        if not self.prompt_file.is_file():
            raise ValueError(f'Unable to find Prompt file: "{self.prompt_file}"')
        try:
            with open(self.prompt_file, "r") as fp:
                json.load(fp)
        except json.JSONDecodeError as e:
            raise ValueError(f'Invalid Json Prompt file "{self.prompt_file}": {e}')

    def run(self) -> dict:
        with open(self.prompt_file, "r") as fp:
            prompts = json.load(fp)

        client_kwargs = self.client_args.copy()
        client_kwargs.update(dict(api_key=self.openai_api_key))
        client = OpenAI(**client_kwargs)

        contents = []
        for prompt in prompts:
            kwargs = self.model_args.copy()
            kwargs.update(dict(messages=prompt))
            logger.debug(f"Message sent: \n{indent(pformat(prompt), '  ')}")
            completion = client.chat.completions.create(model=self.model, **kwargs)

            if len(completion.choices) < 1:
                logger.error(f"No response choice given")
                contents.append("")
            elif completion.choices[0].finish_reason == "length":
                logger.error(f"Response truncated because of finish reason = length")
                contents.append("")
            else:
                logger.debug(f"Response received: \n{indent(completion.choices[0].message.content, '  ')}")
                contents.append(completion.choices[0].message.content)

        response_file = Path(tempfile.mktemp(".json"))
        with open(response_file, "w") as outfile:
            json.dump(contents, outfile, indent=2)

        logger.info(f"Run completed {self.__class__.__name__}")
        return dict(new_code=response_file, openai_responses=contents)
