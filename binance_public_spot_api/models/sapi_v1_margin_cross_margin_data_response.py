from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SapiV1MarginCrossMarginDataResponse(SdkBaseModel):
    vip_level: int = Field(alias="vipLevel")
    coin: str
    transfer_in: bool = Field(alias="transferIn")
    borrowable: bool
    daily_interest: str = Field(alias="dailyInterest")
    yearly_interest: str = Field(alias="yearlyInterest")
    borrow_limit: str = Field(alias="borrowLimit")
    marginable_pairs: list[str] = Field(alias="marginablePairs")


class SapiV1MarginCrossMarginDataResponseDict(TypedDict):
    vip_level: int
    coin: str
    transfer_in: bool
    borrowable: bool
    daily_interest: str
    yearly_interest: str
    borrow_limit: str
    marginable_pairs: list[str]
