from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .profit_today import ProfitToday, ProfitTodayDict
from .profit_yesterday import ProfitYesterday, ProfitYesterdayDict


class Data17(SdkBaseModel):
    fifteen_min_hash_rate: str = Field(alias="fifteenMinHashRate")
    day_hash_rate: str = Field(alias="dayHashRate")
    valid_num: int = Field(alias="validNum")
    invalid_num: int = Field(alias="invalidNum")
    profit_today: ProfitToday = Field(alias="profitToday")
    profit_yesterday: ProfitYesterday = Field(alias="profitYesterday")
    user_name: str = Field(alias="userName")
    unit: str
    algo: str


class Data17Dict(TypedDict):
    fifteen_min_hash_rate: str
    day_hash_rate: str
    valid_num: int
    invalid_num: int
    profit_today: ProfitToday | ProfitTodayDict
    profit_yesterday: ProfitYesterday | ProfitYesterdayDict
    user_name: str
    unit: str
    algo: str
