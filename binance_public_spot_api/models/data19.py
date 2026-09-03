from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_profit1 import AccountProfit1, AccountProfit1Dict


class Data19(SdkBaseModel):
    account_profits: list[AccountProfit1] = Field(alias="accountProfits")
    total_num: int = Field(alias="totalNum")
    page_size: int = Field(alias="pageSize")


class Data19Dict(TypedDict):
    account_profits: list[AccountProfit1 | AccountProfit1Dict]
    total_num: int
    page_size: int
