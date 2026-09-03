from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fill2 import Fill2, Fill2Dict


class ApiV3SorOrderResponse(SdkBaseModel):
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
    working_time: int = Field(alias="workingTime")
    fills: list[Fill2]
    working_floor: str = Field(alias="workingFloor")
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")
    used_sor: bool = Field(alias="usedSor")


class ApiV3SorOrderResponseDict(TypedDict):
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
    working_time: int
    fills: list[Fill2 | Fill2Dict]
    working_floor: str
    self_trade_prevention_mode: str
    used_sor: bool
