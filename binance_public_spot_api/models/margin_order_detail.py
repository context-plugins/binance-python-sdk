from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MarginOrderDetail(SdkBaseModel):
    client_order_id: str = Field(alias="clientOrderId")
    cummulative_quote_qty: str = Field(alias="cummulativeQuoteQty")
    executed_qty: str = Field(alias="executedQty")
    iceberg_qty: str = Field(alias="icebergQty")
    is_working: bool = Field(alias="isWorking")
    order_id: int = Field(alias="orderId")
    orig_qty: str = Field(alias="origQty")
    price: str
    side: str
    status: str
    stop_price: str = Field(alias="stopPrice")
    symbol: str
    is_isolated: bool = Field(alias="isIsolated")
    time: int
    time_in_force: str = Field(alias="timeInForce")
    type_: str = Field(alias="type")
    update_time: int = Field(alias="updateTime")
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")


class MarginOrderDetailDict(TypedDict):
    client_order_id: str
    cummulative_quote_qty: str
    executed_qty: str
    iceberg_qty: str
    is_working: bool
    order_id: int
    orig_qty: str
    price: str
    side: str
    status: str
    stop_price: str
    symbol: str
    is_isolated: bool
    time: int
    time_in_force: str
    type_: str
    update_time: int
    self_trade_prevention_mode: str
