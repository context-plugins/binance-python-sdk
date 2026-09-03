from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order1 import Order1, Order1Dict
from .order_report6 import OrderReport6, OrderReport6Dict


class SapiV1MarginOrderOtoResponse(SdkBaseModel):
    order_list_id: int = Field(alias="orderListId")
    contingency_type: str = Field(alias="contingencyType")
    list_status_type: str = Field(alias="listStatusType")
    list_order_status: str = Field(alias="listOrderStatus")
    list_client_order_id: str = Field(alias="listClientOrderId")
    transaction_time: int = Field(alias="transactionTime")
    symbol: str
    is_isolated: bool = Field(alias="isIsolated")
    orders: list[Order1]
    order_reports: list[OrderReport6] = Field(alias="orderReports")


class SapiV1MarginOrderOtoResponseDict(TypedDict):
    order_list_id: int
    contingency_type: str
    list_status_type: str
    list_order_status: str
    list_client_order_id: str
    transaction_time: int
    symbol: str
    is_isolated: bool
    orders: list[Order1 | Order1Dict]
    order_reports: list[OrderReport6 | OrderReport6Dict]
