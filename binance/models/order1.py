from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Order1(SdkBaseModel):
    symbol: str
    order_id: int = Field(alias="orderId")
    client_order_id: str = Field(alias="clientOrderId")


class Order1Dict(TypedDict):
    symbol: str
    order_id: int
    client_order_id: str
