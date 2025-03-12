import functools
from abc import ABC, abstractmethod

from pydantic_ai.tools import RunContext
from pydantic_ai.tools import Tool as PydanticTool
from pydantic_ai.tools import ToolDefinition
from typing_extensions import Type

from patchwork.logger import logger


class Tool(ABC):
    __internal_map: dict[str, Type["Tool"]] = dict()

    def __init_subclass__(cls, tool_name=None, abc_register=True, tool_logging=True, **kwargs):
        cls_name = tool_name or cls.__name__
        cls.name = cls_name

        if tool_logging:
            setattr(cls, "execute", Tool.__execute_logging_wrapper(cls.__dict__["execute"]))

        if not abc_register:
            return

        if cls_name in cls.__internal_map.keys():
            raise ValueError(f"Duplicate subclass name for class {cls.__name__}: {cls_name}")
        Tool.__internal_map[cls_name] = cls

    @property
    @abstractmethod
    def json_schema(self) -> dict:
        ...

    @abstractmethod
    def execute(self, *args, **kwargs) -> str:
        ...

    @staticmethod
    def get_tools(**kwargs) -> dict[str, "Tool"]:
        rv = dict()
        for k, v in Tool.__internal_map.items():
            try:
                rv[k] = v(**kwargs)
            except Exception as e:
                continue

        return rv

    @staticmethod
    def get_description(tooling: "Tool") -> str:
        return tooling.json_schema.get("description", "")

    @staticmethod
    def get_parameters(tooling: "Tool") -> str:
        return ", ".join(tooling.json_schema.get("required", []))

    def to_pydantic_ai_function_tool(self) -> PydanticTool[None]:
        async def _prep(ctx: RunContext[None], tool_def: ToolDefinition) -> ToolDefinition:
            tool_def.parameters_json_schema = self.json_schema.get("input_schema", {})
            return tool_def

        return PydanticTool(
            self.execute, prepare=_prep, name=self.name, description=self.json_schema.get("description", "")
        )

    @staticmethod
    def __execute_logging_wrapper(func):
        @functools.wraps(func)
        def execute_logging_wrapper(self, *args, **kwargs):
            arg_text = ""
            if len(args) > 0:
                arg_text += f"args: {args}"
            if len(kwargs) > 0:
                arg_text += f"kwargs: {kwargs}"

            logger.info(f"Executing Tool: {self.name} with {arg_text}")
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                logger.error(f"Error executing Tool: {self.name}: {e}")
                return f"Error: {e}"

        return execute_logging_wrapper
