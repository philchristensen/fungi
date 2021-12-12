# -*- coding: utf-8 -*-
import os
from typing import Any

import opensea

def get_collection(slug:str) -> Any:
    api = opensea.OpenseaAPI(apikey=os.environ["OPENSEA_API_KEY"])
    return api.collection(collection_slug=slug)
