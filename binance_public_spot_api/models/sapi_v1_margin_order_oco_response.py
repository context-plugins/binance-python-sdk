from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .order1 import Order1, Order1Dict
from .order_report5 import OrderReport5, OrderReport5Dict


class SapiV1MarginOrderOcoResponse(SdkBaseModel):
    order_list_id: int = Field(alias="orderListId")
    contingency_type: str = Field(alias="contingencyType")
    list_status_type: str = Field(alias="listStatusType")
    list_order_status: str = Field(alias="listOrderStatus")
    list_client_order_id: str = Field(alias="listClientOrderId")
    transaction_time: int = Field(alias="transactionTime")
    symbol: str
    margin_buy_borrow_amount: str = Field(alias="marginBuyBorrowAmount")
    """will not return if no margin trade happens"""

    margin_buy_borrow_asset: str = Field(alias="marginBuyBorrowAsset")
    """will not return if no margin trade happens"""

    is_isolated: bool = Field(alias="isIsolated")
    orders: list[Order1]
    order_reports: list[OrderReport5] = Field(alias="orderReports")


class SapiV1MarginOrderOcoResponseDict(TypedDict):
    order_list_id: int
    contingency_type: str
    list_status_type: str
    list_order_status: str
    list_client_order_id: str
    transaction_time: int
    symbol: str
    margin_buy_borrow_amount: str
    margin_buy_borrow_asset: str
    is_isolated: bool
    orders: list[Order1 | Order1Dict]
    order_reports: list[OrderReport5 | OrderReport5Dict]
