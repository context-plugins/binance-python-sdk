from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MarginOrderResponseAck(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    client_order_id: str = Field(alias="clientOrderId")
    is_isolated: bool = Field(alias="isIsolated")
    transact_time: int = Field(alias="transactTime")


class MarginOrderResponseAckDict(TypedDict):
    symbol: str
    order_id: int
    client_order_id: str
    is_isolated: bool
    transact_time: int
