from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row49(SdkBaseModel):
    amount: str
    product_id: str = Field(alias="productId")
    asset: str
    create_time: int = Field(alias="createTime")
    type_: str = Field(alias="type")
    product_name: str = Field(alias="productName")
    order_id: int = Field(alias="orderId")


class Row49Dict(TypedDict):
    amount: str
    product_id: str
    asset: str
    create_time: int
    type_: str
    product_name: str
    order_id: int
