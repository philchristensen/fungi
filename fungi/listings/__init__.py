# -*- coding: utf-8 -*-
"""
Click-specific code to define a CLI.
"""
import logging
from typing import List, Any

import click
import tabulate

from ..core import models, opensea

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
    result: List[Any] = [True]
    try:
        with models.Session.begin() as session:
            while(result):
                for asset in opensea.get_collection_assets(session, slug, offset=page):
                    if count % 500 == 0:
                        log.info(f"Scanned {count} records so far, found {len(table)} orders...")
                    if asset.details['sell_orders'] is not None:
                        for order in asset.details['sell_orders']:
                            table.append(dict(
                                token_id = asset.details['token_id'],
                                created_date = order['created_date'],
                                base_price = int(order['base_price']) / 10**18
                            ))
                    count += 1
                    page += 1
    except KeyboardInterrupt:
        pass
    click.echo(tabulate.tabulate(table, headers="keys"))
