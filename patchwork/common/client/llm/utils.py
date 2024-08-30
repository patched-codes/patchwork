from __future__ import annotations

from openai.lib._parsing._completions import type_to_response_format_param
from openai.types.chat.completion_create_params import ResponseFormat
from pydantic import BaseModel, Field, create_model
from typing_extensions import List

from patchwork.logger import logger


def base_model_to_schema(base_model: BaseModel) -> ResponseFormat:
    return type_to_response_format_param(base_model)


def example_json_to_base_model(json_example: str | None) -> BaseModel | None:
    if json_example is None:
        return None

    try:
        example_data = loads(json_example)
    except Exception as e:
        logger.error(f"Failed to parse example json", e)
        return None

    return example_dict_to_base_model(example_data)


def example_dict_to_base_model(example_data: dict) -> BaseModel:
    base_model_field_defs: dict[str, tuple[type | BaseModel, Field]] = dict()
    for example_data_key, example_data_value in example_data.items():
        if isinstance(example_data_value, dict):
            value_typing = example_dict_to_base_model(example_data_value)
        elif isinstance(example_data_value, list):
            nested_value = example_data_value[0]
            if isinstance(nested_value, dict):
                nested_typing = example_dict_to_base_model(nested_value)
            else:
                nested_typing = type(nested_value)
            value_typing = List[nested_typing]
        else:
            value_typing = type(example_data_value)

        field_kwargs = dict()
        if value_typing == str:
            field_kwargs["description"] = example_data_value

        field = Field(**field_kwargs)
        base_model_field_defs[example_data_key] = (value_typing, field)

    model = create_model("ResponseFormat", **base_model_field_defs)
    return model
