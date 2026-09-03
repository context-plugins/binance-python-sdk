from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OrderResponseAck(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    order_list_id: int = Field(alias="orderListId")
    client_order_id: str = Field(alias="clientOrderId")
    transact_time: int = Field(alias="transactTime")


class OrderResponseAckDict(TypedDict):
    symbol: str
    order_id: int
    order_list_id: int
    client_order_id: str
    transact_time: int
