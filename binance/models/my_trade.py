from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MyTrade(SdkBaseModel):
    symbol: str
    id: int
    """Trade id"""

    order_id: int = Field(alias="orderId")
    order_list_id: int = Field(alias="orderListId")
    price: str
    """Price"""

    qty: str
    """Amount of base asset"""

    quote_qty: str = Field(alias="quoteQty")
    """Amount of quote asset"""

    commission: str
    commission_asset: str = Field(alias="commissionAsset")
    time: int
    """Trade timestamp"""

    is_buyer: bool = Field(alias="isBuyer")
    is_maker: bool = Field(alias="isMaker")
    is_best_match: bool = Field(alias="isBestMatch")


class MyTradeDict(TypedDict):
    symbol: str
    id: int
    order_id: int
    order_list_id: int
    price: str
    qty: str
    quote_qty: str
    commission: str
    commission_asset: str
    time: int
    is_buyer: bool
    is_maker: bool
    is_best_match: bool
