import importlib
import importlib.util
import json
import traceback
from collections import deque
from pathlib import Path
from types import ModuleType

import click
import yaml
from click import echo
from git import Repo
from typing_extensions import Iterable

from patchwork.common.client.patched import PatchedClient
from patchwork.logger import init_cli_logger, logger
from patchwork.steps.PreparePrompt import PreparePrompt

_DATA_FORMAT_MAPPING = {
    "yaml": yaml.dump,
    "json": json.dumps,
}

_CONFIG_NAME = "config.yml"
_PROMPT_NAME = "prompt.json"
_PATCHFLOW_MODULE_NAME = "patchwork.patchflows"


def _get_config_path(config: str | None, patchflow: str) -> Path | None:
    config_path = Path(config)
    if config_path.is_dir():
        patchwork_path = config_path / patchflow
        if patchwork_path.is_dir():
            return patchwork_path


def _get_patchflow_names(base_path: Path | str | None) -> Iterable[str]:
    names = []
    if base_path is None:
        return names

    base_path = Path(base_path)
    if not base_path.is_dir():
        return names

    for path in base_path.iterdir():
        if path.is_dir() and (path / f"{path.name}.py").is_file():
            names.append(path.name)
    return names


def list_option_callback(ctx: click.Context, param: click.Parameter, value: str | None) -> None:
    if not value or ctx.resilient_parsing:
        return

    patchflows = []
    default_path = Path(__file__).parent / "patchflows"
    patchflows.extend(_get_patchflow_names(default_path))

    config_path = ctx.params.get("config")
    patchflows.extend(_get_patchflow_names(config_path))

    echo("\n".join(patchflows), color=ctx.color)
    ctx.exit()


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.version_option(message="%(version)s", package_name="patchwork-cli")
@click.help_option("-h", "--help")
@click.option(
    "--config",
    is_eager=True,
    type=click.Path(exists=True, dir_okay=True, resolve_path=True, file_okay=True),
    help="Path to the configurations folder, see https://github.com/patched-codes/patchwork-configs for examples.",
)
@click.option(
    "-l",
    "--list",
    is_flag=True,
    expose_value=False,
    callback=list_option_callback,
    help="Show a list of available patchflows, see https://docs.patched.codes/patchflows/patchflows for details.",
)
@click.option(
    "--log",
    hidden=True,
    default="INFO",
    type=click.Choice(
        [
            "CRITICAL",
            "FATAL",
            "ERROR",
            "WARNING",
            "WARN",
            "INFO",
            "DEBUG",
        ],
        case_sensitive=False,
    ),
    is_eager=True,
    callback=lambda x, y, z: init_cli_logger(z),
)
@click.argument("patchflow", nargs=1, required=True)
@click.argument("opts", nargs=-1, type=click.UNPROCESSED, required=False)
@click.option(
    "--output",
    type=click.Path(exists=False, resolve_path=True, writable=True),
    help="Path to the output file which contains the state after the patchflow finishes.",
)
@click.option(
    "data_format", "--format", type=click.Choice(["yaml", "json"]), default="json", help="Format of the output file."
)
@click.option("patched_api_key", "--patched_api_key", help="API key to use with the patched.codes service.")
def cli(
    log: str,
    patchflow: str,
    opts: list[str],
    config: str | None,
    output: str | None,
    data_format: str,
    patched_api_key: str | None,
):
    if "::" in patchflow:
        module_path, _, patchflow_name = patchflow.partition("::")
    else:
        patchflow_name = patchflow
        module_path = _PATCHFLOW_MODULE_NAME

    possbile_module_paths = deque((module_path,))

    inputs = {}
    if patched_api_key is not None:
        try:
            inputs["patched_api_key"] = patched_api_key
            PatchedClient(patched_api_key).verify_api_key()  # assuming this method exists for verifying the API key
        except Exception:
            logger.error("Invalid API key")
            return

    # rest of the code here...


if __name__ == "__main__":
    cli()
