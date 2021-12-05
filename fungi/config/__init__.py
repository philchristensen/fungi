# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""

import click

@click.group()
def config() -> None:
    """
    Configure the application.
    """

@config.command(name="set")
def set_config() -> None:
    """
    Set a configuration value.
    """

@config.command(name="get")
def get_config() -> None:
    """
    Get a configuration value.
    """
