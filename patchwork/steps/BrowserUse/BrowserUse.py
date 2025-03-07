import asyncio
import logging
import os
from datetime import datetime

from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
from patchwork.steps.BrowserUse.typed import BrowserUseInputs, BrowserUseOutputs
from patchwork.steps.SimplifiedLLMOnce.SimplifiedLLMOnce import SimplifiedLLMOnce

logger = logging.getLogger(__name__)

# Global variables to cache browser initialization
_browser = None
_controller = None


def init_browser():
    """
    Initialize and cache browser and controller instances.

    This function uses a singleton pattern to ensure we only create one browser
    instance throughout the application lifecycle, which saves resources.

    Returns:
        tuple: (Browser, Controller) instances for web automation
    """
    global _browser, _controller

    # Return cached instances if already initialized
    if _browser is not None and _controller is not None:
        return _browser, _controller

    from browser_use import Browser, BrowserConfig, BrowserContextConfig, Controller
    from browser_use.agent.views import ActionResult
    from browser_use.browser.context import BrowserContext

    # Set up downloads directory for browser operations
    downloads_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    context_config = BrowserContextConfig(save_downloads_path=downloads_path)
    config = BrowserConfig(headless=True, disable_security=True, new_context_config=context_config)
    controller = Controller()

    # Register custom action to upload files to web elements
    @controller.action(
        description="Upload file to interactive element with file path",
    )
    async def upload_file(index: int, path: str, browser: BrowserContext):
        """
        Upload a file to a file input element identified by its index.

        Args:
            index: The DOM element index to target
            path: Local file path to upload
            browser: Browser context for interaction

        Returns:
            ActionResult: Result of the upload operation
        """
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

    # Register custom action to read file contents
    @controller.action(description="Read the file content of a file given a path")
    async def read_file(path: str):
        """
        Read and return the contents of a file at the specified path.

        Args:
            path: Path to the file to read

        Returns:
            ActionResult: File contents or error message
        """
        if not os.path.exists(path):
            return ActionResult(error=f"File {path} does not exist")

        with open(path, "r") as f:
            content = f.read()
        msg = f"File content: {content}"
        logger.info(msg)
        return ActionResult(extracted_content=msg, include_in_memory=True)

    # Cache the initialized instances
    _browser = Browser(config=config)
    _controller = controller

    return _browser, _controller


class BrowserUse(Step, input_class=BrowserUseInputs, output_class=BrowserUseOutputs):
    """
    Step implementation for browser automation tasks.

    This class provides a high-level interface for executing browser-based tasks
    using various LLM providers (Google, OpenAI, Anthropic) to control the browser.
    """

    required_keys = {"task"}

    def __init__(self, inputs):
        """
        Initialize the BrowserUse step with configuration inputs.

        Args:
            inputs: Dictionary containing configuration parameters (see: BrowserUseInputs)
        """
        super().__init__(inputs)

        if not all(key in inputs.keys() for key in self.required_keys):
            raise ValueError(f'Missing required data: "{self.required_keys}"')

        # Configure the appropriate LLM based on provided API keys
        if "google_api_key" in self.inputs:
            from langchain_google_genai import ChatGoogleGenerativeAI

            self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=self.inputs["google_api_key"])
        elif "openai_api_key" in self.inputs:
            from langchain_openai import ChatOpenAI

            self.llm = ChatOpenAI(model="gpt-4o", api_key=self.inputs["openai_api_key"])
        elif "anthropic_api_key" in self.inputs:
            from langchain_anthropic import ChatAnthropic

            self.llm = ChatAnthropic(
                model="claude-3-7-sonnet-latest",
                api_key=self.inputs["anthropic_api_key"],
            )

        # Configure GIF generation for debugging/visualization
        self.generate_gif = (
            f"agent_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.gif"
            if ("generate_gif" in self.inputs and self.inputs["generate_gif"])
            or ("debug" in self.inputs and self.inputs["debug"])
            else False
        )

    def run(self) -> dict:
        """
        Execute the browser automation task.

        This method initializes the browser agent, runs the specified task,
        and returns the results, optionally formatting them as JSON.

        Returns:
            dict: Results of the browser automation task
        """
        from browser_use import Agent

        browser, controller = init_browser()
        agent = Agent(
            browser=browser,
            controller=controller,
            task=mustache_render(self.inputs["task"], self.inputs["task_value"]),
            llm=self.llm,
            generate_gif=self.generate_gif,
            validate_output=True,
        )

        # Run the agent in an event loop
        loop = asyncio.new_event_loop()
        self.history = loop.run_until_complete(agent.run())

        # Format results as JSON if schema provided
        if "example_json" in self.inputs:
            return self.__format_history_as_json()

        return {
            "history": self.history,
            "result": self.history.final_result(),
            "generated_gif": self.generate_gif,
        }

    def __format_history_as_json(self):
        """
        Format browser history as JSON using an LLM.

        Uses the same LLM provider as the main task to convert
        the browser history into a structured JSON format based
        on the provided schema.

        Returns:
            dict: Formatted JSON result
        """
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
