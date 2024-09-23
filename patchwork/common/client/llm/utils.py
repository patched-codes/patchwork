from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Type

from openai.lib._parsing._completions import type_to_response_format_param
from openai.types.chat.completion_create_params import ResponseFormat
from pydantic import BaseModel, Field, create_model
from typing_extensions import List

from patchwork.logger import logger


def json_schema_to_model(json_schema: Dict[str, Any]) -> Type[BaseModel]:
    model_name = json_schema.get("title")

    field_definitions = dict()
    for name, prop in json_schema.get("properties", {}).items():
        required = json_schema.get("required", [])
        field_type = __json_schema_to_pydantic_type(prop)
        field_definition = Field(description=json_schema.get("description"), default=... if name in required else None)
        field_definitions[name] = (field_type, field_definition)

    return create_model(model_name, **field_definitions)


def __json_schema_to_pydantic_type(json_schema: Dict[str, Any]) -> type:
    type_ = json_schema.get("type")

    if type_ == "string":
        return str
    elif type_ == "integer":
        return int
    elif type_ == "number":
        return float
    elif type_ == "boolean":
        return bool
    elif type_ == "array":
        items_schema = json_schema.get("items")
        if items_schema:
            item_type = __json_schema_to_pydantic_type(items_schema)
            return List[item_type]
        else:
            return List
    elif type_ == "object":
        # Handle nested models.
        properties = json_schema.get("properties")
        if properties:
            nested_model = json_schema_to_model(json_schema)
            return nested_model
        else:
            return Dict
    elif type_ == "null":
        return Optional[Any]  # Use Optional[Any] for nullable fields
    else:
        raise ValueError(f"Unsupported JSON schema type: {type_}")


def example_json_to_schema(json_example: str | dict | None) -> ResponseFormat | None:
    if json_example is None:
        return None

    base_model = None
    if isinstance(json_example, str):
        base_model = __example_string_to_base_model(json_example)
    elif isinstance(json_example, dict):
        base_model = __example_dict_to_base_model(json_example)

    if base_model is None:
        return None

    return base_model_to_schema(base_model)


def base_model_to_schema(base_model: Type[BaseModel]) -> ResponseFormat:
    return type_to_response_format_param(base_model)


def __example_string_to_base_model(json_example: str) -> Type[BaseModel] | None:
    try:
        example_data = json.loads(json_example)
    except Exception as e:
        logger.error(f"Failed to parse example json", e)
        return None

    return __example_dict_to_base_model(example_data)


def __example_dict_to_base_model(example_data: dict) -> Type[BaseModel]:
    base_model_field_defs: dict[str, tuple[type | BaseModel, Field]] = dict()
    for example_data_key, example_data_value in example_data.items():
        if isinstance(example_data_value, dict):
            value_typing = __example_dict_to_base_model(example_data_value)
        elif isinstance(example_data_value, list):
            nested_value = example_data_value[0]
            if isinstance(nested_value, dict):
                nested_typing = __example_dict_to_base_model(nested_value)
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

    return create_model("ResponseFormat", **base_model_field_defs)


def truncate_message(message: str, direction_callback) -> str:
    direction = direction_callback(message)
    if direction >= 0:
        return message

    max_guess = len(message)
    min_guess = 1
    return _truncate_message(message, direction_callback, min_guess, max_guess)


def _truncate_message(message, direction_callback, min_guess, max_guess):
    change = int((max_guess - min_guess) / 2)
    guess = min_guess + change
    vector = direction_callback(message[:guess])
    if vector == 0:
        return message[:guess]
    print(f"min_guess: {min_guess}, max_guess: {max_guess}, change: {change}, vector: {vector}")
    if vector > 0:
        min_guess = guess
    else:
        max_guess = guess

    return _truncate_message(message, direction_callback, min_guess, max_guess)

# TODO: Add tests for truncate_message
# if __name__ == "__main__":
    # import random
    # import string
    # for i in range(1, 1000):
    #     text = "".join(random.choices(string.ascii_lowercase, k=random.choice(range(i, i + 20))))
    #     print(f"Truncating {text} to {text[:i]}")
    #     new = truncate_message(text, lambda x: i - len(x))
    #     assert text[:i] == new
    #     print(f"Truncated {text} to {new}")
