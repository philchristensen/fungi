# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""
import json
import logging

import click

from ..core import opensea

log = logging.getLogger(__name__)

@click.group()
def collection() -> None:
    """
    Interact with different OpenSea collections.
    """

@collection.command(name="get")
@click.argument('slug')
def get_collection(slug: str) -> None:
    """
    Get an OpenSea collection.
    """
    result = opensea.get_collection(slug)
    click.echo(json.dumps(result))
