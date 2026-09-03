from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order1 import Order1, Order1Dict


class SapiV1MarginAllOrderListResponse(SdkBaseModel):
    order_list_id: int = Field(alias="orderListId")
    contingency_type: str = Field(alias="contingencyType")
    list_status_type: str = Field(alias="listStatusType")
    list_order_status: str = Field(alias="listOrderStatus")
    list_client_order_id: str = Field(alias="listClientOrderId")
    transaction_time: int = Field(alias="transactionTime")
    symbol: str
    is_isolated: bool = Field(alias="isIsolated")
    orders: list[Order1]


class SapiV1MarginAllOrderListResponseDict(TypedDict):
    order_list_id: int
    contingency_type: str
    list_status_type: str
    list_order_status: str
    list_client_order_id: str
    transaction_time: int
    symbol: str
    is_isolated: bool
    orders: list[Order1 | Order1Dict]
