from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginIsolatedAllPairsResponse(SdkBaseModel):
    symbol: str
    base: str
    quote: str
    is_margin_trade: bool = Field(alias="isMarginTrade")
    is_buy_allowed: bool = Field(alias="isBuyAllowed")
    is_sell_allowed: bool = Field(alias="isSellAllowed")


class SapiV1MarginIsolatedAllPairsResponseDict(TypedDict):
    symbol: str
    base: str
    quote: str
    is_margin_trade: bool
    is_buy_allowed: bool
    is_sell_allowed: bool
