# -*- coding: utf-8 -*-
"""
Interact with the raritysniper API.
"""

from typing import Dict, Any

import requests

ALIASES = {
    "acidheadz" : "acid-headz"
}

def get_rarity(asset: Any) -> str:
    guess = asset['asset_contract']['symbol'].lower()
    slug = ALIASES.get(guess, guess)
    token_id = asset['token_id']
    response = requests.get(f"https://api.raritysniper.com/public/collection/{slug}/id/{token_id}")
    data = response.json()
    return str(data.get("rank", "n/a"))
