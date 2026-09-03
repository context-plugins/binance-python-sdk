from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class List2(SdkBaseModel):
    quote_id: str = Field(alias="quoteId")
    order_id: int = Field(alias="orderId")
    order_status: str = Field(alias="orderStatus")
    from_asset: str = Field(alias="fromAsset")
    from_amount: str = Field(alias="fromAmount")
    to_asset: str = Field(alias="toAsset")
    to_amount: str = Field(alias="toAmount")
    ratio: str
    """price ratio"""

    inverse_ratio: str = Field(alias="inverseRatio")
    """inverse price"""

    create_time: int = Field(alias="createTime")


class List2Dict(TypedDict):
    quote_id: str
    order_id: int
    order_status: str
    from_asset: str
    from_amount: str
    to_asset: str
    to_amount: str
    ratio: str
    inverse_ratio: str
    create_time: int
