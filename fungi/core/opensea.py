# -*- coding: utf-8 -*-
"""
Interact with the raritysniper API.
"""

from typing import Any
import logging

import opensea

from ..config import store
from .models import Asset, dbcache

log = logging.getLogger(__name__)

def get_collection(slug:str) -> Any:
    apikey = store.get_value("opensea.api-key")
    api = opensea.OpenseaAPI(apikey=apikey)
    return api.collection(collection_slug=slug)

@dbcache(Asset)
def get_collection_assets(slug:str, offset:int = 0) -> Any:
    apikey = store.get_value("opensea.api-key")
    api = opensea.OpenseaAPI(apikey=apikey)
    c = api.collection(collection_slug=slug)
    contract = c["collection"]["primary_asset_contracts"][0]["address"]
    return api.assets(asset_contract_address=contract, offset=offset)['assets']

@dbcache(Asset)
def get_wallet_assets(slug:str, offset:int = 0) -> Any:
    apikey = store.get_value("opensea.api-key")
    api = opensea.OpenseaAPI(apikey=apikey)
    wallet = store.get_value(f"ethwallets.{slug}")
    return api.assets(owner=wallet, offset=offset)['assets']
