from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OrderDetails(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    order_list_id: int = Field(alias="orderListId")
    """Unless OCO, value will be -1"""

    client_order_id: str = Field(alias="clientOrderId")
    price: str
    orig_qty: str = Field(alias="origQty")
    executed_qty: str = Field(alias="executedQty")
    cummulative_quote_qty: str = Field(alias="cummulativeQuoteQty")
    status: str
    time_in_force: str = Field(alias="timeInForce")
    type_: str = Field(alias="type")
    side: str
    stop_price: str = Field(alias="stopPrice")
    iceberg_qty: str = Field(alias="icebergQty")
    time: int
    update_time: int = Field(alias="updateTime")
    is_working: bool = Field(alias="isWorking")
    working_time: int = Field(alias="workingTime")
    orig_quote_order_qty: str = Field(alias="origQuoteOrderQty")
    self_trade_prevention_mode: str = Field(alias="selfTradePreventionMode")
    prevented_match_id: Optional[int] = Field(default=UNSET, alias="preventedMatchId")
    prevented_quantity: Optional[str] = Field(default=UNSET, alias="preventedQuantity")


class OrderDetailsDict(TypedDict):
    symbol: str
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
    stop_price: str
    iceberg_qty: str
    time: int
    update_time: int
    is_working: bool
    working_time: int
    orig_quote_order_qty: str
    self_trade_prevention_mode: str
    prevented_match_id: NotRequired[int]
    prevented_quantity: NotRequired[str]
