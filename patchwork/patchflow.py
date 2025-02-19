import abc

import click
from typing_extensions import Type

_internal_map: dict[str, Type["Patchflow"]]


class PatchflowCommands(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted(list(_internal_map.keys()))

    def get_command(self, ctx, name):
        return _internal_map.get(name, None)


class Patchflow(abc.ABC, click.MultiCommand):
    def __init_subclass__(cls, patchflow_name=None, steps=None, **kwargs):
        name = patchflow_name or cls.__name__
        _internal_map[name] = cls

    @abc.abstractmethod
    def run(self) -> dict:
        """
        Runs the step.
        :return: a dictionary of outputs
        """
        ...
