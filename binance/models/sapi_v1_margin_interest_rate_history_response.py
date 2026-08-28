from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginInterestRateHistoryResponse(SdkBaseModel):
    asset: str
    daily_interest_rate: str = Field(alias="dailyInterestRate")
    timestamp: int
    vip_level: int = Field(alias="vipLevel")


class SapiV1MarginInterestRateHistoryResponseDict(TypedDict):
    asset: str
    daily_interest_rate: str
    timestamp: int
    vip_level: int
