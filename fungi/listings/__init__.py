# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""
import json

import click

from ..core import opensea

@click.group()
def listings() -> None:
    """
    Fetch OpenSea listings.
    """

@listings.command(name="get")
@click.argument('slug')
def get_listings(slug: str) -> None:
    """
    Get all OpenSea listings for a collection.
    """
    # result = opensea.get_collection(slug)
    # click.echo(json.dumps(result))
