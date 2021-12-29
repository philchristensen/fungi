# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""
from typing import List, Any

import click
import tabulate

from ..core import models, opensea, raritysniper

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
    result: List[Any]  = [True]
    with models.Session.begin() as session:
        while(result):
            result = opensea.get_wallet_assets(session, slug, offset=page)
            for asset in result:
                table.append(dict(
                    name = asset.name,
                    rarity_rank = raritysniper.get_rarity(asset)
                ))
                page += 1
        click.echo(tabulate.tabulate(table, headers="keys"))
