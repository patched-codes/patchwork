import asyncio
import logging
import os
from datetime import datetime

from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step
from patchwork.steps.BrowserUse.typed import BrowserUseInputs, BrowserUseOutputs
from patchwork.steps.SimplifiedLLMOnce.SimplifiedLLMOnce import SimplifiedLLMOnce

logger = logging.getLogger(__name__)


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
        from browser_use import BrowserConfig
        from patchwork.common.utils.browser_initializer import BrowserInitializer

        browser_config = BrowserConfig(headless=self.inputs.get("headless", True), disable_security=True)
        browser_context = BrowserInitializer.init_browser_context(browser_config)
        controller = BrowserInitializer.init_controller()
        logger.info("Browser initialized")
        agent = Agent(
            browser_context=browser_context,
            controller=controller,
            task=mustache_render(self.inputs["task"], self.inputs["task_value"]),
            llm=self.llm,
            generate_gif=self.generate_gif,
            validate_output=True,
            initial_actions=self.inputs.get("initial_actions", None),
        )

        # Run the agent in an event loop
        loop = asyncio.new_event_loop()
        self.history = loop.run_until_complete(agent.run())
        loop.run_until_complete(browser_context.close())
        loop.run_until_complete(browser_context.browser.close())
        loop.close()

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
