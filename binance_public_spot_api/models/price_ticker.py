from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PriceTicker(SdkBaseModel):
    symbol: str
    price: str


class PriceTickerDict(TypedDict):
    symbol: str
    price: str
