# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""
import logging
from typing import List, Any

import click
import tabulate

from ..core import opensea

log = logging.getLogger(__name__)

@click.group()
def listings() -> None:
    """
    Fetch OpenSea listings.
    """

@listings.command(name="get")
@click.argument('slug')
def get_listings(slug: str) -> None:
    """
    List sales in an OpenSea collection.
    """
    table: List[Any] = []
    count = 1
    page = 0
    result = {'assets': [True]}
    try:
        while(result['assets']):
            result = opensea.get_collection_assets(slug, offset=page)
            for asset in result['assets']:
                if count % 500 == 0:
                    log.info(f"Scanned {count} records so far, found {len(table)} orders...")
                if asset['sell_orders'] is not None:  # type: ignore
                    for order in asset['sell_orders']:  # type: ignore
                        table.append(dict(
                            token_id = asset['token_id'],  # type: ignore
                            created_date = order['created_date'],
                            base_price = int(order['base_price']) / 10**18
                        ))
                count += 1
                page += 1
    except KeyboardInterrupt:
        pass
    click.echo(tabulate.tabulate(table, headers="keys"))
