from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_order1 import SubOrder1, SubOrder1Dict


class SapiV1AlgoSpotSubOrdersResponse(SdkBaseModel):
    total: int
    executed_qty: str = Field(alias="executedQty")
    executed_amt: str = Field(alias="executedAmt")
    sub_orders: list[SubOrder1] = Field(alias="subOrders")


class SapiV1AlgoSpotSubOrdersResponseDict(TypedDict):
    total: int
    executed_qty: str
    executed_amt: str
    sub_orders: list[SubOrder1 | SubOrder1Dict]
