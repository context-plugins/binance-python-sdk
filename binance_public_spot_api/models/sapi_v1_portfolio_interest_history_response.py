from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1PortfolioInterestHistoryResponse(SdkBaseModel):
    asset: str
    interest: str
    interest_accrued_time: int = Field(alias="interestAccruedTime")
    interest_rate: str = Field(alias="interestRate")
    principal: str


class SapiV1PortfolioInterestHistoryResponseDict(TypedDict):
    asset: str
    interest: str
    interest_accrued_time: int
    interest_rate: str
    principal: str
