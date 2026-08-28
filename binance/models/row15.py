from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row15(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    flexible_daily_interest_rate: str = Field(alias="_flexibleDailyInterestRate")
    flexible_yearly_interest_rate: str = Field(alias="_flexibleYearlyInterestRate")
    d_daily_interest_rate30: str = Field(alias="_30dDailyInterestRate")
    d_yearly_interest_rate30: str = Field(alias="_30dYearlyInterestRate")
    d_daily_interest_rate60: str = Field(alias="_60dDailyInterestRate")
    d_yearly_interest_rate60: str = Field(alias="_60dYearlyInterestRate")
    min_limit: str = Field(alias="minLimit")
    max_limit: str = Field(alias="maxLimit")
    vip_level: int = Field(alias="vipLevel")


class Row15Dict(TypedDict):
    loan_coin: str
    flexible_daily_interest_rate: str
    flexible_yearly_interest_rate: str
    d_daily_interest_rate30: str
    d_yearly_interest_rate30: str
    d_daily_interest_rate60: str
    d_yearly_interest_rate60: str
    min_limit: str
    max_limit: str
    vip_level: int
