import importlib
import json
import traceback
from pathlib import Path

import click
import yaml

from patchwork.logger import init_cli_logger, logger


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.version_option(message="%(version)s")
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
    try:
        module = importlib.import_module(f".patchflows", "patchwork")
    except ModuleNotFoundError:
        logger.debug(f"Patchflow {patchflow} not found")
        exit(1)

    try:
        patchflow_class = getattr(module, patchflow)
    except AttributeError:
        logger.debug(f"Patchflow {patchflow} not found as a class in {Path(__file__).parent / 'patchflows'}")
        exit(1)

    inputs = {}
    if config is not None:
        config_path = Path(config)
        if config_path.is_dir():
            patchwork_config_path = config_path / patchflow / "config.yml"
            if not patchwork_config_path.exists() or not patchwork_config_path.is_file():
                logger.error(f'Config file "{patchwork_config_path}" not found from directory "{config}"')
                exit(1)
            config_path = patchwork_config_path
        inputs = yaml.safe_load(config_path.read_text())

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

    data_format_mapping = {
        "yaml": yaml.dump,
        "json": json.dumps,
    }

    if output is not None:
        serialize = data_format_mapping.get(data_format, json.dumps)
        with open(output, "w") as file:
            file.write(serialize(inputs))


if __name__ == "__main__":
    cli()
