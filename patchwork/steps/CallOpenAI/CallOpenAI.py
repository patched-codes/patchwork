import json
import os
import tempfile
from pathlib import Path
from pprint import pformat
from textwrap import indent

from openai import OpenAI

from patchwork.logger import logger
from patchwork.step import Step

_TOKEN_URL = "https://app.patched.codes/signin"
_DEFAULT_PATCH_URL = "https://patchwork.patched.codes/v1"


class CallOpenAI(Step):
    required_keys = {"prompt_file"}

    def __init__(self, inputs: dict):
        logger.info(f"Run started {self.__class__.__name__}")

        # Set 'openai_key' from inputs or environment if not already set
        inputs.setdefault("openai_api_key", os.environ.get("OPENAI_API_KEY"))

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.model = inputs["model"]
        self.model_args = {key[len("model_") :]: value for key, value in inputs.items() if key.startswith("model_")}
        self.client_args = {key[len("client_") :]: value for key, value in inputs.items() if key.startswith("client_")}

        openai_key = inputs.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
        if openai_key is not None:
            self.openai_api_key = openai_key

        patched_key = inputs.get("patched_api_key")
        if patched_key is not None:
            self.openai_api_key = patched_key
            self.client_args["base_url"] = _DEFAULT_PATCH_URL

        if self.openai_api_key is None:
            raise ValueError(
                f"Model API key not found.\n"
                f'Please login at: "{_TOKEN_URL}",\n'
                "Please go to the Integration's tab and generate an API key.\n"
                "Please copy the access token that is generated, "
                "and add `--patched_api_key=<token>` to the command line.\n"
                "\n"
                "If you are using a OpenAI API Key, please set `--openai_api_key=<token>`.\n"
            )

        if not self.openai_api_key:
            raise ValueError('Missing required data: "openai_api_key"')

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
