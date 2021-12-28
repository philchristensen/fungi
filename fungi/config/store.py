# -*- coding: utf-8 -*-
"""
Config store support code.
"""

import os
from configparser import ConfigParser
from pathlib import Path
from typing import Any

def get_value(key: str) -> Any:
    config = get_config()
    if '.' not in key:
        key = f"DEFAULT.{key}"
    ns, key = key.split('.', maxsplit=1)
    return config[ns][key]

def get_config() -> ConfigParser:
    """
    Syntactic sugar to get the path to the config file.
    """
    config_path = Path("~/.fungi/config").expanduser()
    config = ConfigParser()
    if(os.path.exists(config_path)):
        with open(config_path, 'r') as f:
            config.read_file(f)
    return config

def save_config(config: ConfigParser) -> None:
    config_path = Path("~/.fungi").expanduser()
    if not config_path.exists():
        config_path.mkdir()
    with open(config_path.joinpath('config'), 'w') as f:
        config.write(f)
