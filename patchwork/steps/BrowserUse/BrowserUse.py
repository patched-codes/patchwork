import asyncio
import logging
import os

from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig, Controller
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from datetime import datetime

from patchwork.step import Step
from patchwork.steps import SimplifiedLLMOnce
from patchwork.steps.BrowserUse.typed import BrowserUseInputs, BrowserUseOutputs

downloads_path = os.path.join(os.getcwd(), "downloads")
logger = logging.getLogger(__name__)
context_config = BrowserContextConfig(save_downloads_path=downloads_path)
config = BrowserConfig(
    headless=True, disable_security=True, new_context_config=context_config
)
controller = Controller()

if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


@controller.action(
    description="Upload file to interactive element with file path",
)
async def upload_file(index: int, path: str, browser: BrowserContext):
    if not os.path.exists(path):
        return ActionResult(error=f"File {path} does not exist")

    dom_el = await browser.get_dom_element_by_index(index)
    file_upload_dom_el = dom_el.get_file_upload_element()

    if file_upload_dom_el is None:
        msg = f"No file upload element found at index {index}. The element may be hidden or not an input type file"
        logger.info(msg)
        return ActionResult(error=msg)

    file_upload_el = await browser.get_locate_element(file_upload_dom_el)

    if file_upload_el is None:
        msg = f"No file upload element found at index {index}. The element may be hidden or not an input type file"
        logger.info(msg)
        return ActionResult(error=msg)

    try:
        await file_upload_el.set_input_files(path)
        msg = f"Successfully uploaded file to index {index}"
        logger.info(msg)
        return ActionResult(extracted_content=msg, include_in_memory=True)
    except Exception as e:
        msg = f"Failed to upload file to index {index}: {str(e)}"
        logger.info(msg)
        return ActionResult(error=msg)


@controller.action(description="Read the file content of a file given a path")
async def read_file(path: str):
    if not os.path.exists(path):
        return ActionResult(error=f"File {path} does not exist")

    with open(path, "r") as f:
        content = f.read()
    msg = f"File content: {content}"
    logger.info(msg)
    return ActionResult(extracted_content=msg, include_in_memory=True)


class BrowserUse(Step, input_class=BrowserUseInputs, output_class=BrowserUseOutputs):
    required_keys = {"task"}

    def __init__(self, inputs):
        super().__init__(inputs)

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        self.browser = Browser(config=config)

        if "google_api_key" in self.inputs:
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash", google_api_key=self.inputs["google_api_key"]
            )
        elif "openai_api_key" in self.inputs:
            self.llm = ChatOpenAI(model="gpt-4o", api_key=self.inputs["openai_api_key"])
        elif "anthropic_api_key" in self.inputs:
            self.llm = ChatAnthropic(
                model="claude-3-7-sonnet-latest",
                api_key=self.inputs["anthropic_api_key"],
            )
        self.generate_gif = (
            f"agent_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.gif"
            if ("generate_gif" in self.inputs and self.inputs["generate_gif"])
            or ("debug" in self.inputs and self.inputs["debug"])
            else False
        )

    def run(self) -> dict:
        agent = Agent(
            browser=self.browser,
            task=self.inputs["task"],
            llm=self.llm,
            generate_gif=self.generate_gif,
            validate_output=True,
            controller=controller,
        )

        loop = asyncio.new_event_loop()
        self.history = loop.run_until_complete(agent.run())
        if "example_json" in self.inputs:
            return self.__format_history_as_json()

        return {
            "history": self.history,
            "result": self.history.final_result(),
            "generated_gif": self.generate_gif,
        }

    def __format_history_as_json(self):
        inputs = dict(
            user_prompt=f"""
You are a helpful assistant that formats a history of browser actions and conversations into a JSON object.
You are provided with a JSON schema for the history.
Only include the JSON object in your response, nothing else.

Here is the history:
<history>
{self.history.final_result()}
</history>
""",
            json_schema=self.inputs["example_json"],
            prompt_value=dict(),
        )

        if "google_api_key" in self.inputs:
            inputs["google_api_key"] = self.inputs["google_api_key"]
            inputs["model"] = "gemini-2.0-flash"
        elif "openai_api_key" in self.inputs:
            inputs["openai_api_key"] = self.inputs["openai_api_key"]
            inputs["model"] = "gpt-4o-mini"
        elif "anthropic_api_key" in self.inputs:
            inputs["anthropic_api_key"] = self.inputs["anthropic_api_key"]
            inputs["model"] = "claude-3-5-haiku-latest"
        return SimplifiedLLMOnce(inputs).run()
