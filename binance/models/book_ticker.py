from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BookTicker(SdkBaseModel):
    symbol: str
    bid_price: str = Field(alias="bidPrice")
    bid_qty: str = Field(alias="bidQty")
    ask_price: str = Field(alias="askPrice")
    ask_qty: str = Field(alias="askQty")


class BookTickerDict(TypedDict):
    symbol: str
    bid_price: str
    bid_qty: str
    ask_price: str
    ask_qty: str
