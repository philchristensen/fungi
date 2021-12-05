# -*- coding: utf-8 -*-
"""
Config store support code.
"""

import os
from configparser import ConfigParser
from pathlib import Path

def get_config() -> ConfigParser:
    """
    Syntactic sugar to get the path to the config file.
    """
    config_path = Path("~/.fungi").expanduser()
    config = ConfigParser()
    if(os.path.exists(config_path)):
        with open(config_path, 'r') as f:
            config.read_file(f)
    return config

def save_config(config: ConfigParser) -> None:
    config_path = Path("~/.fungi").expanduser()
    with open(config_path, 'w') as f:
        config.write(f)
