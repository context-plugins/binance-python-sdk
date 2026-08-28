from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginAllPairsResponse(SdkBaseModel):
    base: str
    id: int
    is_buy_allowed: bool = Field(alias="isBuyAllowed")
    is_margin_trade: bool = Field(alias="isMarginTrade")
    is_sell_allowed: bool = Field(alias="isSellAllowed")
    quote: str
    symbol: str


class SapiV1MarginAllPairsResponseDict(TypedDict):
    base: str
    id: int
    is_buy_allowed: bool
    is_margin_trade: bool
    is_sell_allowed: bool
    quote: str
    symbol: str
