from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MarginOrder(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    orig_client_order_id: str = Field(alias="origClientOrderId")
    client_order_id: str = Field(alias="clientOrderId")
    price: str
    orig_qty: str = Field(alias="origQty")
    executed_qty: str = Field(alias="executedQty")
    cummulative_quote_qty: str = Field(alias="cummulativeQuoteQty")
    status: str
    time_in_force: str = Field(alias="timeInForce")
    type_: str = Field(alias="type")
    side: str


class MarginOrderDict(TypedDict):
    symbol: str
    order_id: int
    orig_client_order_id: str
    client_order_id: str
    price: str
    orig_qty: str
    executed_qty: str
    cummulative_quote_qty: str
    status: str
    time_in_force: str
    type_: str
    side: str
