import importlib
import textwrap

from typing_extensions import (
    Annotated,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypedDict,
    get_args,
    get_origin,
    get_type_hints,
)

from patchwork.step import Step


class StepTypeConfig(object):
    def __init__(
        self,
        is_config: bool = False,
        is_path: bool = False,
        and_op: List[str] = None,
        or_op: List[str] = None,
        xor_op: List[str] = None,
        msg: str = "",
    ):
        self.is_config = is_config
        self.is_path: bool = is_path
        self.and_op: List[str] = and_op or []
        self.or_op: List[str] = or_op or []
        self.xor_op: List[str] = xor_op or []
        self.msg: str = msg


def validate_steps_with_inputs(keys: Iterable[str], *steps: Type[Step]) -> None:
    current_keys = set(keys)
    report = {}
    for step in steps:
        output_keys, step_report = validate_step_with_inputs(current_keys, step)
        current_keys = current_keys.union(output_keys)
        report[step.__name__] = step_report

    has_error = any(len(value) > 0 for value in report.values())
    if not has_error:
        return

    error_message = "Invalid inputs for steps:\n"
    for step_name, step_report in sorted(report.items(), key=lambda x: x[0]):
        if len(step_report) > 0:
            error_message += f"Step: {step_name}\n"
            for key, msg in step_report.items():
                error_message += f"  - {key}: \n{textwrap.indent(msg, '      ')}\n"
    raise ValueError(error_message)


__NOT_GIVEN = TypedDict


def validate_step_type_config_with_inputs(
    key_name: str, input_keys: Set[str], step_type_config: StepTypeConfig
) -> Tuple[bool, str]:
    is_key_set = key_name in input_keys

    and_keys = set(step_type_config.and_op)
    if len(and_keys) > 0:
        missing_and_keys = sorted(and_keys.difference(input_keys))
        if is_key_set and len(missing_and_keys) > 0:
            return (
                False,
                step_type_config.msg
                or f"Missing required input data because {key_name} is set: {', '.join(missing_and_keys)}",
            )

    or_keys = set(step_type_config.or_op)
    if len(or_keys) > 0:
        missing_or_keys = or_keys.difference(input_keys)
        if not is_key_set and len(missing_or_keys) == len(or_keys):
            return (
                False,
                step_type_config.msg
                or f"Missing required input: At least one of {', '.join(sorted([key_name, *or_keys]))} has to be set",
            )

    xor_keys = set(step_type_config.xor_op)
    if len(xor_keys) > 0:
        missing_xor_keys = xor_keys.difference(input_keys)
        if not is_key_set and len(missing_xor_keys) == len(xor_keys):
            return (
                False,
                step_type_config.msg or f"Missing required input: Exactly one of {', '.join(xor_keys)} has to be set",
            )
        elif is_key_set and len(missing_xor_keys) < len(xor_keys) - 1:
            conflicting_keys = xor_keys.intersection(input_keys)
            return (
                False,
                step_type_config.msg
                or f"Excess input data: {', '.join(sorted(conflicting_keys))} cannot be set at the same time",
            )

    return True, step_type_config.msg


def validate_step_with_inputs(input_keys: Set[str], step: Type[Step]) -> Tuple[Set[str], Dict[str, str]]:
    module_path, _, _ = step.__module__.rpartition(".")
    step_name = step.__name__
    type_module = importlib.import_module(f"{module_path}.typed")
    step_input_model = getattr(type_module, f"{step_name}Inputs", __NOT_GIVEN)
    step_output_model = getattr(type_module, f"{step_name}Outputs", __NOT_GIVEN)
    if step_input_model is __NOT_GIVEN:
        raise ValueError(f"Missing input model for step {step_name}")
    if step_output_model is __NOT_GIVEN:
        raise ValueError(f"Missing output model for step {step_name}")

    step_report = {}
    for key in step_input_model.__required_keys__:
        if key not in input_keys:
            step_report[key] = f"Missing required input data"
            continue

    step_type_hints = get_type_hints(step_input_model, include_extras=True)
    for key, field_info in step_type_hints.items():
        step_type_config = find_step_type_config(field_info)
        if step_type_config is None:
            continue

        if key in step_report.keys():
            step_report[key] = step_type_config.msg or f"Missing required input data"
            continue

        is_ok, msg = validate_step_type_config_with_inputs(key, input_keys, step_type_config)
        if not is_ok:
            step_report[key] = msg

    return set(step_output_model.__required_keys__), step_report


def find_step_type_config(python_type: type) -> Optional[StepTypeConfig]:
    annotated = find_annotated(python_type)
    if annotated is None:
        return None
    for metadata in annotated.__metadata__:
        if metadata.__class__.__name__ == StepTypeConfig.__name__:
            return metadata

    return None


def find_annotated(python_type: Type) -> Optional[Type[Annotated]]:
    origin = get_origin(python_type)
    args = get_args(python_type)
    if origin is Annotated:
        return python_type

    if len(args) > 0:
        for arg in args:
            possible_step_type_config = find_annotated(arg)
            if possible_step_type_config is not None:
                return possible_step_type_config

    return None
