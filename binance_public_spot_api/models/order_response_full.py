from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fill import Fill, FillDict


class OrderResponseFull(SdkBaseModel):
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
    strategy_id: Optional[int] = Field(default=UNSET, alias="strategyId")
    strategy_type: Optional[int] = Field(default=UNSET, alias="strategyType")
    working_time: int = Field(alias="workingTime")
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")
    fills: list[Fill]


class OrderResponseFullDict(TypedDict):
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
    strategy_id: NotRequired[int]
    strategy_type: NotRequired[int]
    working_time: int
    self_trade_prevention_mode: str
    fills: list[Fill | FillDict]
