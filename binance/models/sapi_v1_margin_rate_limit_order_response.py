from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginRateLimitOrderResponse(SdkBaseModel):
    rate_limit_type: str = Field(alias="rateLimitType")
    interval: str
    interval_num: int = Field(alias="intervalNum")
    limit: int
    count: int


class SapiV1MarginRateLimitOrderResponseDict(TypedDict):
    rate_limit_type: str
    interval: str
    interval_num: int
    limit: int
    count: int
