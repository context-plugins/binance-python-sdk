from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ConvertAcceptQuoteResponse(SdkBaseModel):
    order_id: str = Field(alias="orderId")
    create_time: int = Field(alias="createTime")
    order_status: str = Field(alias="orderStatus")


class SapiV1ConvertAcceptQuoteResponseDict(TypedDict):
    order_id: str
    create_time: int
    order_status: str
