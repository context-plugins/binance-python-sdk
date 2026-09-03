from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MarginOrderResponseResult(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    client_order_id: str = Field(alias="clientOrderId")
    transact_time: int = Field(alias="transactTime")
    price: str
    orig_qty: str = Field(alias="origQty")
    executed_qty: str = Field(alias="executedQty")
    cummulative_quote_qty: str = Field(alias="cummulativeQuoteQty")
    status: str
    time_in_force: str = Field(alias="timeInForce")
    type_: str = Field(alias="type")
    is_isolated: bool = Field(alias="isIsolated")
    side: str


class MarginOrderResponseResultDict(TypedDict):
    symbol: str
    order_id: int
    client_order_id: str
    transact_time: int
    price: str
    orig_qty: str
    executed_qty: str
    cummulative_quote_qty: str
    status: str
    time_in_force: str
    type_: str
    is_isolated: bool
    side: str
