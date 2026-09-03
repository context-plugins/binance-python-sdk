from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiV3RateLimitOrderResponse(SdkBaseModel):
    rate_limit_type: str = Field(alias="rateLimitType")
    interval: str
    interval_num: int = Field(alias="intervalNum")
    limit: int
    count: Optional[int] = UNSET


class ApiV3RateLimitOrderResponseDict(TypedDict):
    rate_limit_type: str
    interval: str
    interval_num: int
    limit: int
    count: NotRequired[int]
