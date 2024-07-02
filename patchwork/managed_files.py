from pathlib import Path

import click

HOME_FOLDER = Path(click.get_app_dir("Patched", force_posix=True))
__LOG_NAME = "patched.log"
LOG_FILE = HOME_FOLDER / __LOG_NAME
__CONFIG_NAME = "config.json"
CONFIG_FILE = HOME_FOLDER / __CONFIG_NAME
