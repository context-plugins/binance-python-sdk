from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_order import SubOrder, SubOrderDict


class SapiV1AlgoFuturesSubOrdersResponse(SdkBaseModel):
    total: int
    executed_qty: str = Field(alias="executedQty")
    executed_amt: str = Field(alias="executedAmt")
    sub_orders: list[SubOrder] = Field(alias="subOrders")


class SapiV1AlgoFuturesSubOrdersResponseDict(TypedDict):
    total: int
    executed_qty: str
    executed_amt: str
    sub_orders: list[SubOrder | SubOrderDict]
