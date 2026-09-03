from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ConvertOrderStatusResponse(SdkBaseModel):
    order_id: int = Field(alias="orderId")
    order_status: str = Field(alias="orderStatus")
    from_asset: str = Field(alias="fromAsset")
    from_amount: str = Field(alias="fromAmount")
    to_asset: str = Field(alias="toAsset")
    to_amount: str = Field(alias="toAmount")
    ratio: str
    inverse_ratio: str = Field(alias="inverseRatio")
    create_time: int = Field(alias="createTime")


class SapiV1ConvertOrderStatusResponseDict(TypedDict):
    order_id: int
    order_status: str
    from_asset: str
    from_amount: str
    to_asset: str
    to_amount: str
    ratio: str
    inverse_ratio: str
    create_time: int
