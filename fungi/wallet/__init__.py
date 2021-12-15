# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""
from typing import List, Any

import click
import tabulate

from ..core import opensea, raritysniper

@click.group()
def wallet() -> None:
    """
    Work with my wallets.
    """

@wallet.command(name="get")
@click.argument('slug', default="__all__")
def get_wallet(slug: str) -> None:
    """
    Get all OpenSea listings for a wallet.
    """
    table: List[Any] = []
    page = 0
    result = {'assets': [True]}
    while(result['assets']):
        result = opensea.get_wallet_assets(slug, offset=page)
        for asset in result['assets']:
            #breakpoint()
            table.append(dict(
                name = asset['name'],  # type: ignore
                rarity_rank = raritysniper.get_rarity(asset)
            ))
            page += 1
    click.echo(tabulate.tabulate(table, headers="keys"))
