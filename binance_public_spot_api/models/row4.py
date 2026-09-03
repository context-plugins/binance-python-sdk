from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row4(SdkBaseModel):
    avg_price: str = Field(alias="avgPrice")
    executed_qty: str = Field(alias="executedQty")
    order_id: int = Field(alias="orderId")
    price: str
    qty: str
    side: str
    symbol: str
    time_in_force: str = Field(alias="timeInForce")
    is_isolated: bool = Field(alias="isIsolated")
    updated_time: int = Field(alias="updatedTime")


class Row4Dict(TypedDict):
    avg_price: str
    executed_qty: str
    order_id: int
    price: str
    qty: str
    side: str
    symbol: str
    time_in_force: str
    is_isolated: bool
    updated_time: int
