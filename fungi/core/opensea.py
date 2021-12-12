# -*- coding: utf-8 -*-
from typing import Any

import opensea

from ..config import store

def get_collection(slug:str) -> Any:
    api = opensea.OpenseaAPI(apikey=store.get_value("opensea.api-key"))
    return api.collection(collection_slug=slug)
