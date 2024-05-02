import importlib
from collections import defaultdict
from functools import partial
from types import ModuleType

import yaml
from typing_extensions import _TypedDictMeta, get_type_hints


def filter_attr(module_type: ModuleType, attr: str) -> bool:
    if attr.startswith("__"):
        return False

    clazz_type = getattr(module_type, attr)
    if not isinstance(clazz_type, _TypedDictMeta):
        return False

    return True


def adjust(module_hints) -> dict:
    adjusted_hints = defaultdict(dict)
    for k, v in module_hints.items():
        is_inputs = k.endswith("Inputs")
        is_outputs = k.endswith("Outputs")
        if not is_inputs and not is_outputs:
            continue

        step_name = k.removesuffix("Inputs").removesuffix("Outputs")

        if is_inputs:
            adjusted_hints[step_name]["inputs"] = dict(
                required=list(v["required"].keys()),
                optional=list(v["optional"].keys()),
            )
        else:
            adjusted_hints[step_name]["outputs"] = list(v["required"].keys())

    return dict(adjusted_hints)


def main():
    sub_module = importlib.import_module(f"patchwork.steps")
    module_hints = {}
    for name in dir(sub_module):
        if name.startswith("__"):
            continue

        try:
            module = importlib.import_module(f"patchwork.steps.{name}.typed")
        except ModuleNotFoundError:
            continue

        types = filter(partial(filter_attr, module), dir(module))
        for t in types:
            clazz = getattr(module, t)
            hints = get_type_hints(clazz)
            required_keys = clazz.__required_keys__
            optional_keys = clazz.__optional_keys__
            module_hints[t] = dict(
                required={k: hints[k] for k in required_keys},
                optional={k: hints[k] for k in optional_keys},
            )

    module_hints = adjust(module_hints)

    return module_hints


if __name__ == "__main__":
    print(yaml.dump(main()))
