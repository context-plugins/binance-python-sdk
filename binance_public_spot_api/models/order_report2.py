from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OrderReport2(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    order_list_id: int = Field(alias="orderListId")
    client_order_id: str = Field(alias="clientOrderId")
    transact_time: int = Field(alias="transactTime")
    price: str
    orig_qty: str = Field(alias="origQty")
    executed_qty: str = Field(alias="executedQty")
    cummulative_quote_qty: str = Field(alias="cummulativeQuoteQty")
    status: str
    time_in_force: str = Field(alias="timeInForce")
    type_: str = Field(alias="type")
    side: str
    stop_price: str = Field(alias="stopPrice")
    working_time: int = Field(alias="workingTime")
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")


class OrderReport2Dict(TypedDict):
    symbol: str
    order_id: int
    order_list_id: int
    client_order_id: str
    transact_time: int
    price: str
    orig_qty: str
    executed_qty: str
    cummulative_quote_qty: str
    status: str
    time_in_force: str
    type_: str
    side: str
    stop_price: str
    working_time: int
    self_trade_prevention_mode: str
