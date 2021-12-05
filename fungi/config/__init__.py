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
