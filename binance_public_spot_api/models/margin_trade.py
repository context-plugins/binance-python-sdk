from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MarginTrade(SdkBaseModel):
    commission: str
    commission_asset: str = Field(alias="commissionAsset")
    id: int
    is_best_match: bool = Field(alias="isBestMatch")
    is_buyer: bool = Field(alias="isBuyer")
    is_maker: bool = Field(alias="isMaker")
    order_id: int = Field(alias="orderId")
    price: str
    qty: str
    symbol: str
    is_isolated: bool = Field(alias="isIsolated")
    time: int


class MarginTradeDict(TypedDict):
    commission: str
    commission_asset: str
    id: int
    is_best_match: bool
    is_buyer: bool
    is_maker: bool
    order_id: int
    price: str
    qty: str
    symbol: str
    is_isolated: bool
    time: int
