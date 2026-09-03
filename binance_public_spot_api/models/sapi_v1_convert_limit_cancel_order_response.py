from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1ConvertLimitCancelOrderResponse(SdkBaseModel):
    order_id: int = Field(alias="orderId")
    status: str


class SapiV1ConvertLimitCancelOrderResponseDict(TypedDict):
    order_id: int
    status: str
