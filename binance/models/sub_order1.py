from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubOrder1(SdkBaseModel):
    algo_id: int = Field(alias="algoId")
    order_id: int = Field(alias="orderId")
    order_status: str = Field(alias="orderStatus")
    executed_qty: str = Field(alias="executedQty")
    executed_amt: str = Field(alias="executedAmt")
    fee_amt: str = Field(alias="feeAmt")
    fee_asset: str = Field(alias="feeAsset")
    book_time: int = Field(alias="bookTime")
    avg_price: str = Field(alias="avgPrice")
    side: str
    symbol: str
    sub_id: int = Field(alias="subId")
    time_in_force: str = Field(alias="timeInForce")
    orig_qty: str = Field(alias="origQty")


class SubOrder1Dict(TypedDict):
    algo_id: int
    order_id: int
    order_status: str
    executed_qty: str
    executed_amt: str
    fee_amt: str
    fee_asset: str
    book_time: int
    avg_price: str
    side: str
    symbol: str
    sub_id: int
    time_in_force: str
    orig_qty: str
