from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CancelResponse(SdkBaseModel):
    symbol: str
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
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")
    transact_time: Optional[int] = Field(default=UNSET, alias="transactTime")


class CancelResponseDict(TypedDict):
    symbol: str
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
    self_trade_prevention_mode: str
    transact_time: NotRequired[int]
