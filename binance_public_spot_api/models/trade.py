from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Trade(SdkBaseModel):
    id: int
    """trade id"""

    price: str
    """price"""

    qty: str
    """amount of base asset"""

    quote_qty: str = Field(alias="quoteQty")
    """amount of quote asset"""

    time: int
    """Trade executed timestamp, as same as ``T`` in the stream"""

    is_buyer_maker: bool = Field(alias="isBuyerMaker")
    is_best_match: bool = Field(alias="isBestMatch")


class TradeDict(TypedDict):
    id: int
    price: str
    qty: str
    quote_qty: str
    time: int
    is_buyer_maker: bool
    is_best_match: bool
