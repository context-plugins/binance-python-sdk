from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Data7(SdkBaseModel):
    order_no: str = Field(alias="orderNo")
    fiat_currency: str = Field(alias="fiatCurrency")
    indicated_amount: str = Field(alias="indicatedAmount")
    amount: str
    total_fee: str = Field(alias="totalFee")
    method: str
    status: str
    """Processing, Failed, Successful, Finished, Refunding, Refunded, Refund Failed, Order Partial credit Stopped"""

    create_time: int = Field(alias="createTime")
    update_time: int = Field(alias="updateTime")


class Data7Dict(TypedDict):
    order_no: str
    fiat_currency: str
    indicated_amount: str
    amount: str
    total_fee: str
    method: str
    status: str
    create_time: int
    update_time: int
