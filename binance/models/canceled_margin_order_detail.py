from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CanceledMarginOrderDetail(SdkBaseModel):
    symbol: str
    is_isolated: bool = Field(alias="isIsolated")
    orig_client_order_id: str = Field(alias="origClientOrderId")
    order_id: int = Field(alias="orderId")
    order_list_id: int = Field(alias="orderListId")
    client_order_id: str = Field(alias="clientOrderId")
    price: str
    orig_qty: str = Field(alias="origQty")
    executed_qty: str = Field(alias="executedQty")
    cummulative_quote_qty: str = Field(alias="cummulativeQuoteQty")
    status: str
    time_in_force: str = Field(alias="timeInForce")
    type_: str = Field(alias="type")
    side: str


class CanceledMarginOrderDetailDict(TypedDict):
    symbol: str
    is_isolated: bool
    orig_client_order_id: str
    order_id: int
    order_list_id: int
    client_order_id: str
    price: str
    orig_qty: str
    executed_qty: str
    cummulative_quote_qty: str
    status: str
    time_in_force: str
    type_: str
    side: str
