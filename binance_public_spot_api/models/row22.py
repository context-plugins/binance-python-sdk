from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Row22(SdkBaseModel):
    loan_coin: str = Field(alias="loanCoin")
    d_hourly_interest_rate7: str = Field(alias="_7dHourlyInterestRate")
    d_daily_interest_rate7: str = Field(alias="_7dDailyInterestRate")
    d_hourly_interest_rate14: str = Field(alias="_14dHourlyInterestRate")
    d_daily_interest_rate14: str = Field(alias="_14dDailyInterestRate")
    d_hourly_interest_rate30: str = Field(alias="_30dHourlyInterestRate")
    d_daily_interest_rate30: str = Field(alias="_30dDailyInterestRate")
    d_hourly_interest_rate90: str = Field(alias="_90dHourlyInterestRate")
    d_daily_interest_rate90: str = Field(alias="_90dDailyInterestRate")
    d_hourly_interest_rate180: str = Field(alias="_180dHourlyInterestRate")
    d_daily_interest_rate180: str = Field(alias="_180dDailyInterestRate")
    min_limit: str = Field(alias="minLimit")
    max_limit: str = Field(alias="maxLimit")
    vip_level: int = Field(alias="vipLevel")


class Row22Dict(TypedDict):
    loan_coin: str
    d_hourly_interest_rate7: str
    d_daily_interest_rate7: str
    d_hourly_interest_rate14: str
    d_daily_interest_rate14: str
    d_hourly_interest_rate30: str
    d_daily_interest_rate30: str
    d_hourly_interest_rate90: str
    d_daily_interest_rate90: str
    d_hourly_interest_rate180: str
    d_daily_interest_rate180: str
    min_limit: str
    max_limit: str
    vip_level: int
