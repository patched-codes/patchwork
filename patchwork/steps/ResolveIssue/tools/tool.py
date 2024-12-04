from abc import ABC, abstractmethod
from typing import Type


class Tool(ABC):
    __internal_map: dict[str, Type["Tool"]] = dict()

    def __init_subclass__(cls, **kwargs):
        cls_name = kwargs.get("name", cls.__name__)
        if cls_name in cls.__internal_map.keys():
            raise ValueError(f"Duplicate subclass name for class {cls.__name__}: {cls_name}")
        cls.name = cls_name
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
        for k, v in kwargs.items():
            try:
                rv[k] = v(**kwargs)
            except Exception as e:
                continue

        return rv

    @staticmethod
    def get_description(tooling: "ToolProtocol") -> str:
        return tooling.json_schema.get("description", "")

    @staticmethod
    def get_parameters(tooling: "ToolProtocol") -> str:
        return ", ".join(tooling.json_schema.get("required", []))
