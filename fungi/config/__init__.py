# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""

import click

from . import store

@click.group()
def config() -> None:
    """
    Configure the application.
    """

@config.command(name="set")
@click.argument('key')
@click.argument('value')
def set_config(key: str, value: str) -> None:
    """
    Set a configuration value.
    """
    s = store.get_config()
    if '.' not in key:
        key = f"DEFAULT.{key}"
    ns, key = key.split('.', maxsplit=1)
    if ns not in s:
        s[ns] = {}
    s[ns][key] = value
    store.save_config(s)

@config.command(name="get")
@click.argument('key')
def get_config(key: str) -> None:
    """
    Get a configuration value.
    """
    value = store.get_value(key)
    click.echo(value)
