import asyncio

from browser_use import Agent, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from datetime import datetime

from patchwork.step import Step
from patchwork.steps import SimplifiedLLMOnce
from patchwork.steps.BrowserUse.typed import BrowserUseInputs, BrowserUseOutputs

config = BrowserConfig(headless=True, disable_security=True)


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
        )

        loop = asyncio.new_event_loop()
        self.history = loop.run_until_complete(agent.run())

        if self.inputs["json_example_schema"]:
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
            json_schema=self.inputs["json_example_schema"],
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
