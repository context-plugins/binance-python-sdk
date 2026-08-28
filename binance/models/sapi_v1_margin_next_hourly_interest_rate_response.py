from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginNextHourlyInterestRateResponse(SdkBaseModel):
    asset: str
    next_hourly_interest_rate: str = Field(alias="nextHourlyInterestRate")


class SapiV1MarginNextHourlyInterestRateResponseDict(TypedDict):
    asset: str
    next_hourly_interest_rate: str
