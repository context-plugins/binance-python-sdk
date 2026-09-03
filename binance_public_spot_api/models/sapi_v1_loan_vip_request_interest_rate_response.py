from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1LoanVipRequestInterestRateResponse(SdkBaseModel):
    asset: str
    flexible_daily_interest_rate: str = Field(alias="flexibleDailyInterestRate")
    flexible_yearly_interest_rate: str = Field(alias="flexibleYearlyInterestRate")
    time: int


class SapiV1LoanVipRequestInterestRateResponseDict(TypedDict):
    asset: str
    flexible_daily_interest_rate: str
    flexible_yearly_interest_rate: str
    time: int
