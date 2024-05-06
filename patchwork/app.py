import importlib
import importlib.util
import json
import traceback
from pathlib import Path
from types import ModuleType

import click
import yaml

from patchwork.logger import init_cli_logger, logger
from patchwork.steps.PreparePrompt import PreparePrompt

_DATA_FORMAT_MAPPING = {
    "yaml": yaml.dump,
    "json": json.dumps,
}


def _get_config_path(config: str, patchflow: str) -> tuple[Path | None, Path | None]:
    config_path = Path(config)
    prompt_path = None
    if config_path.is_dir():
        patchwork_config_path = config_path / patchflow / "config.yml"
        patchwork_prompt_path = config_path / patchflow / "prompt.json"
        config_path = None

        if patchwork_config_path.is_file():
            config_path = patchwork_config_path
        else:
            logger.warning(
                f'Config file "{patchwork_config_path}" not found from directory "{config}", using default config'
            )

        if patchwork_prompt_path.is_file():
            prompt_path = patchwork_prompt_path
        else:
            logger.warning(
                f'Prompt file "{patchwork_prompt_path}" not found from directory "{config}", using default prompt'
            )

    return config_path, prompt_path


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.version_option(message="%(version)s", package_name="patchwork-cli")
@click.help_option("-h", "--help")
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
@click.option("--config", type=click.Path(exists=True, dir_okay=True, resolve_path=True, file_okay=True))
@click.option("--output", type=click.Path(exists=False, resolve_path=True, writable=True), help="Output data file")
@click.option("data_format", "--format", type=click.Choice(["yaml", "json"]), default="json", help="Output data format")
def cli(log: str, patchflow: str, opts: list[str], config: str | None, output: str | None, data_format: str):
    if "::" not in patchflow:
        patchflow = "patchwork.patchflows::" + patchflow

    module_path, _, patchflow_name = patchflow.partition("::")
    module = find_module(module_path, patchflow)

    try:
        patchflow_class = getattr(module, patchflow_name)
    except AttributeError:
        logger.debug(f"Patchflow {patchflow} not found as a class in {module_path}")
        exit(1)

    inputs = {}
    if config is not None:
        config_path, prompt_path = _get_config_path(config, patchflow_name)
        if config_path is None and prompt_path is None:
            exit(1)

        if config_path is not None:
            inputs = yaml.safe_load(config_path.read_text())
        if prompt_path is not None:
            inputs[PreparePrompt.PROMPT_TEMPLATE_FILE_KEY] = prompt_path

    for opt in opts:
        key, equal_sign, value = opt.partition("=")
        key = key.lstrip("-")

        if equal_sign == "":
            # treat --key as a flag
            inputs[key] = True
        else:
            # treat --key=value as a key-value pair
            inputs[key] = value
    try:
        patchflow_instance = patchflow_class(inputs)
        patchflow_instance.run()
    except Exception as e:
        logger.debug(traceback.format_exc())
        logger.error(f"Error running patchflow {patchflow}: {e}")
        exit(1)

    if output is not None:
        serialize = _DATA_FORMAT_MAPPING.get(data_format, json.dumps)
        with open(output, "w") as file:
            file.write(serialize(inputs))


def find_module(module_path, patchflow) -> ModuleType:
    try:
        spec = importlib.util.spec_from_file_location("custom_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception:
        logger.debug(f"Patchflow {patchflow} not found as a file/directory in {module_path}")
        module = None

    if module is not None:
        return module

    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        logger.debug(f"Patchflow {patchflow} not found as a module in {module_path}")
        exit(1)

    return module


if __name__ == "__main__":
    cli()
